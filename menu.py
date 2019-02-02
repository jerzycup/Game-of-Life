import pygame
from button import Button
from button import ButtonSetup
from game import Game
from settings import Settings
from Window import Window


class Menu(Window):

    def __init__(self, settings):
        super().__init__(settings)
        self.colour_button = (180, 180, 0)
        self.colour_button_marked = (180, 0, 120)
        self.colour_button_chosen = (0, 50, 200)

    def buttons(self):
        button_setup = ButtonSetup(self.x, self.y, 3)

        start_button = Button(button_setup.position(1), self.colour_button, 'Start')
        settings_button = Button(button_setup.position(2), self.colour_button, 'Settings')
        quit_button = Button(button_setup.position(3), self.colour_button, 'Quit')

        buttons = [start_button, settings_button, quit_button]

        return buttons

    def events(self, event, pos, buttons):
        start_button = buttons[0]
        settings_button = buttons[1]
        quit_button = buttons[2]

        run = True

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if quit_button.marked(pos):
                run = False

            elif start_button.marked(pos):
                Game(self.settings).run()
                run = False

            elif settings_button.marked(pos):
                Settings(self.settings).run()
                run = False

        if event.type == pygame.MOUSEMOTION:
            if quit_button.marked(pos):
                quit_button.colour = self.colour_button_marked

            elif start_button.marked(pos):
                start_button.colour = self.colour_button_marked

            elif settings_button.marked(pos):
                settings_button.colour = self.colour_button_marked

            else:
                quit_button.colour = self.colour_button
                start_button.colour = self.colour_button
                settings_button.colour = self.colour_button

        return run




