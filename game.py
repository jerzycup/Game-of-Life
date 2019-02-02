from Window import Window
from board import Board
from random import randint
import button
import pygame
import menu
import copy
from cell import Cell


class Game(Window):
    def __init__(self, settings):
        super().__init__(settings)
        self.screen_fill = (0, 0, 0)
        self.cell_size = settings[1]
        self.random = settings[2]
        self.aging = settings[3]
        self.board = Board(int(self.y / self.cell_size), int(self.y / self.cell_size))
        self.colour_button = (0, 255, 0)
        self.colour_button_marked = (255, 0, 0)
        self.colour_button_locked = (0, 0, 255)
        self.alive_set = settings[4][0]
        self.born_set = settings[4][1]

    def buttons(self):
        x = self.x - self.y
        y = self.y

        buttons_setup = button.ButtonSetup(x, y, 7)
        startstop_button = button.Button(buttons_setup.position(2), self.colour_button, 'Start')
        clear_button = button.Button(buttons_setup.position(3), self.colour_button, 'Clear')
        turn_button = button.Button(buttons_setup.position(4), self.colour_button, 'Turn')
        random_button = button.Button(buttons_setup.position(5), self.colour_button, 'Random')
        menu_button = button.Button(buttons_setup.position(6), self.colour_button, 'Menu')

        buttons = [startstop_button, clear_button, turn_button, random_button, menu_button]

        for i in range(len(buttons)):
            buttons[i].x = buttons[i].x + self.y

        return buttons

    def random_board(self):
        for o in range(randint(0, int(self.y * self.y / self.cell_size ** 2))):
            self.board.play_field[randint(0, int(self.y / self.cell_size) - 1)]\
            [randint(0, int(self.y / self.cell_size) - 1)].alive = True

    def cell_check(self, x, y):

        counts = 0
        if x != 0 and y != 0:
            for i in range(3):
                for j in range(3):
                    if i != 1 or j != 1:
                        try:
                            if self.board.play_field[x + i - 1][y + j - 1].alive:
                                counts += 1
                        except IndexError:
                            pass

        else:
            for i in range(3):
                if x == 0 and i == 0:
                    pass
                else:
                    for j in range(3):
                        if y == 0 and j == 0:
                            pass
                        else:
                            if i != 1 or j != 1:
                                try:
                                    if self.board.play_field[x + i - 1][y + j - 1].alive:
                                        counts += 1
                                except IndexError:
                                    pass

        return counts

    def turn_aging(self):
        board = copy.deepcopy(self.board)
        for i in range(len(self.board.play_field)):
            for j in range(len(self.board.play_field[0])):
                board.play_field[i][j].alive = False

        for x in range(len(self.board.play_field) ):
            for y in range(len(self.board.play_field[0])):
                counts = self.cell_check(x, y)

                if counts in self.born_set and not self.board.play_field[x][y].alive:
                    board.play_field[x][y] = Cell(True)

                elif counts in self.alive_set and self.board.play_field[x][y].alive:
                    board.play_field[x][y].alive = True
                    board.play_field[x][y].aging()

                elif counts not in self.born_set and counts not in self.alive_set:
                    board.play_field[x][y] = Cell()

        return board

    def turn(self):
        if self.aging:
            board = self.turn_aging()
        else:
            board = Board(int(self.y / self.cell_size), int(self.y / self.cell_size))
            for x in range(len(self.board.play_field)):
                for y in range(len(self.board.play_field[0])):
                    counts = self.cell_check(x, y)

                    if counts in self.born_set and not self.board.play_field[x][y].alive:
                        board.play_field[x][y].alive = True

                    elif counts in self.alive_set and self.board.play_field[x][y].alive:
                        board.play_field[x][y].alive = True

                    elif counts not in self.born_set and counts not in self.alive_set:
                        board.play_field[x][y].alive = False

        return board

    def texts(self, text):
        font = pygame.font.SysFont('arial', int(0.04 * self.y))

        generation_text = font.render('Generations: {}'.format(text[0]), 1, (0, 0, 255))
        clock_text = font.render('Clock: {}'.format(text[1]), 1, (0, 0, 255))

        return [[generation_text, (self.y, 0)], [clock_text, (self.y, int(self.y * 0.94))]]

    def draw_board(self, screen):
        for x in range(len(self.board.play_field)):
            for y in range(len(self.board.play_field[x])):
                if self.board.play_field[x][y].alive:
                    rect = (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                    pygame.draw.rect(screen, tuple(self.board.play_field[x][y].colour), rect)

    def run(self):
        run = True
        pygame.display.set_caption('Game of Life')
        screen = pygame.display.set_mode((self.x, self.y))
        clock = pygame.time.Clock()

        if self.random:
            self.random_board()

        stop = True

        buttons = self.buttons()

        generation = 0
        time = 1
        time_end = 10

        while run:
            text = [generation, time_end]
            texts = self.texts(text)
            screen.fill(self.screen_fill)

            if not stop:
                time += 1
                buttons[2].colour = self.colour_button_locked
                buttons[3].colour = self.colour_button_locked

            screen.fill(self.screen_fill)

            for i in range(len(buttons)):
                buttons[i].draw(screen)

            for j in range(len(texts)):
                screen.blit(texts[j][0], texts[j][1])

            self.draw_board(screen)

            pygame.draw.line(screen, (255, 255, 255), (self.y, 0), (self.y, self.y))

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if buttons[0].marked(pos):
                        if not stop:
                            stop = True
                            buttons[0].text = 'Start'
                            buttons[2].colour = self.colour_button
                            buttons[3].colour = self.colour_button
                        else:
                            stop = False
                            buttons[0].text = 'Stop'

                    if buttons[1].marked(pos):
                        self.board.clear()
                        generation = 0

                    if buttons[2].marked(pos):
                        if stop:
                            self.board = self.turn()
                            generation += 1

                    if buttons[3].marked(pos):
                        if stop:
                            self.board.clear()
                            self.random_board()
                            generation = 0

                    if buttons[4].marked(pos):
                        menu.Menu(self.settings).run()
                        run = False

                    if pos[0] < self. y:
                        x = int(pos[0] / self.cell_size)
                        y = int(pos[1] / self.cell_size)
                        if self.board.play_field[x][y].alive:
                            self.board.play_field[x][y].alive = False
                        else:
                            self.board.play_field[x][y].alive = True

                if event.type == pygame.MOUSEMOTION:
                    for j in range(len(buttons)):
                        buttons[j].colour = self.colour_button

                    for k in range(len(buttons)):
                        if buttons[k].marked(pos):
                            buttons[k].colour = self.colour_button_marked

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if time_end < 60:
                            time_end += 1
                            time = 1

                    if event.key == pygame.K_DOWN:
                        if time_end > 1:
                            time_end -= 1
                            time = 1

            pygame.display.flip()

            if not stop and time == time_end:
                self.board = self.turn()
                generation += 1
                time = 0

            clock.tick(60)
