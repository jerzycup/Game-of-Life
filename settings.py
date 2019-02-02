import pygame
import menu as m
import button as b
from Window import Window
import rules_options as r


class Settings(Window):
    def __init__(self, settings):
        super().__init__(settings)
        self.colour_button = (180, 180, 0)
        self.colour_button_marked = (180, 0, 120)
        self.colour_button_chosen = (0, 50, 200)

    def buttons(self):
        button_setup = b.ButtonSetup(self.x, self.y, rows=6, y_margin=0.02)

        resolution_button = b.Button(button_setup.position(1), self.colour_button, 'resolution')
        cellsize_button = b.Button(button_setup.position(2), self.colour_button, 'cell size')
        if not self.settings[2]:
            random_button = b.Button(button_setup.position(3), self.colour_button, ' no random board')
        else:
            random_button = b.Button(button_setup.position(3), self.colour_button_chosen, 'random board')

        if not self.settings[3]:
            aging_button = b.Button(button_setup.position(4), self.colour_button, 'no cell aging')
        else:
            aging_button = b.Button(button_setup.position(4), self.colour_button_chosen, 'cell aging')

        rules_button = b.Button(button_setup.position(5), self.colour_button, 'rules')
        back_button = b.Button(button_setup.position(6), self.colour_button, 'back')

        buttons = [resolution_button, cellsize_button, random_button, aging_button, rules_button, back_button]

        return buttons

    def events(self, event, pos, buttons):
        resolution_button = buttons[0]
        cellsize_button = buttons[1]
        random_button = buttons[2]
        aging_button = buttons[3]
        rules_button = buttons[4]
        back_button = buttons[5]

        run = True

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_button.marked(pos):
                m.Menu(self.settings).run()
                run = False

            elif random_button.marked(pos):
                if not self.settings[2]:
                    self.settings[2] = True
                    random_button.colour = self.colour_button_chosen
                    random_button.text = 'random board'
                else:
                    self.settings[2] = False
                    random_button.colour = self.colour_button
                    random_button.text = 'no random board'

            elif resolution_button.marked(pos):
                Resolution(self.settings).run()
                run = False

            elif cellsize_button.marked(pos):
                CellSize(self.settings).run()
                run = False

            elif aging_button.marked(pos):
                if not self.settings[3]:
                    self.settings[3] = True
                    aging_button.colour = self.colour_button_chosen
                    aging_button.text = 'cell aging'
                else:
                    self.settings[3] = False
                    aging_button.colour = self.colour_button
                    aging_button.text = 'no cell aging'

            elif rules_button.marked(pos):
                r.RulesOptions(self.settings).run()
                run = False

        if event.type == pygame.MOUSEMOTION:
            if back_button.marked(pos):
                back_button.colour = self.colour_button_marked

            elif random_button.marked(pos):
                random_button.colour = self.colour_button_marked

            elif resolution_button.marked(pos):
                resolution_button.colour = self.colour_button_marked

            elif cellsize_button.marked(pos):
                cellsize_button.colour = self.colour_button_marked

            elif aging_button.marked(pos):
                aging_button.colour = self.colour_button_marked

            elif rules_button.marked(pos):
                rules_button.colour = self.colour_button_marked

            else:
                back_button.colour = self.colour_button
                resolution_button.colour = self.colour_button
                cellsize_button.colour = self.colour_button
                rules_button.colour = self.colour_button
                if self.settings[2]:
                    random_button.colour = self.colour_button_chosen
                if not self.settings[2]:
                    random_button.colour = self.colour_button
                if self.settings[3]:
                    aging_button.colour = self.colour_button_chosen
                if not self.settings[3]:
                    aging_button.colour = self.colour_button

        return run


class Resolution(Window):
    def __init__(self, settings):
        super().__init__(settings)
        self.resolution_options = [(320, 240), (640, 480), (800, 600), (1120, 840), (1600, 1200)]
        self.colour_button_marked = (180, 0, 120)
        self.colour_button_chosen = (0, 50, 200)
        self.colour_button = (180, 180, 0)

    def buttons(self):
        buttons = []
        buttons_setup = b.ButtonSetup(self.x, self.y, len(self.resolution_options) + 1)
        for i in range(len(self.resolution_options)):
            if self.resolution_options[i] == self.settings[0]:
                buttons.append(b.Button(buttons_setup.position(i + 1), self.colour_button_chosen,
                                        str(self.resolution_options[i])))
            else:
                buttons.append(b.Button(buttons_setup.position(i + 1), self.colour_button,
                                        str(self.resolution_options[i])))

        apply_button = b.Button(buttons_setup.position(len(self.resolution_options) + 1), self.colour_button, 'apply')

        buttons.append(apply_button)

        return buttons

    def events(self, event, pos, buttons):
        run = True

        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(buttons) - 1):
                buttons[i].colour = self.colour_button
                if buttons[i].marked(pos):
                    buttons[i].colour = self.colour_button_chosen
                    self.settings[0] = self.resolution_options[i]
                    self.x = self.settings[0][0]
                    self.y = self.settings[0][1]

            if buttons[-1].marked(pos):
                Settings(self.settings).run()
                run = False

        elif event.type == pygame.MOUSEMOTION:
            for j in range(len(buttons)):
                if buttons[j].colour != self.colour_button_chosen:
                    if buttons[j].marked(pos):
                        buttons[j].colour = self.colour_button_marked
                    else:
                        buttons[j].colour = self.colour_button

        return run


class CellSize(Window):
    def __init__(self, settings):
        super().__init__(settings)
        self.cell_size_options = [2, 4, 5, 10, 20, 40, 60, 120]
        self.colour_button = (180, 180, 0)
        self.colour_button_marked = (180, 0, 120)
        self.colour_button_chosen = (0, 50, 200)

    def buttons(self):
        button_setup = b.ButtonSetup(int(self.x / 2), self.y, 5)
        back_button_setup = b.ButtonSetup(self.x, self.y, 5)

        buttons = []

        for i in range(int(len(self.cell_size_options) / 2)):
            size = button_setup.position(i + 1)
            buttons.append(b.Button(size, self.colour_button, str(self.cell_size_options[i])))

        for j in range(int(len(self.cell_size_options) / 2)):
            size = button_setup.position(j + 1)
            size[0] = int(size[0] + self.x / 2)
            buttons.append(b.Button(size, self.colour_button, str(self.cell_size_options[j + int(len(self.cell_size_options) / 2)])))

        back_button = b.Button(back_button_setup.position(5), self.colour_button, 'back')

        for k in range(len(self.cell_size_options)):
            if self.settings[1] == self.cell_size_options[k]:
                buttons[k].colour = self.colour_button_chosen
        buttons.append(back_button)

        return buttons

    def events(self, event, pos, buttons):
        run = True

        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(buttons) - 1):
                buttons[i].colour = self.colour_button
                if buttons[i].marked(pos):
                    buttons[i].colour = self.colour_button_chosen
                    self.settings[1] = self.cell_size_options[i]

            if buttons[-1].marked(pos):
                Settings(self.settings).run()
                run = False

        elif event.type == pygame.MOUSEMOTION:
            for j in range(len(buttons)):
                if buttons[j].colour != self.colour_button_chosen:
                    if buttons[j].marked(pos):
                        buttons[j].colour = self.colour_button_marked
                    else:
                        buttons[j].colour = self.colour_button

        return run
