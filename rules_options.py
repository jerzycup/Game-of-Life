from Window import Window
import button as b
import settings as s
import pygame


class RulesOptions(Window):

    def __init__(self, settings):
        super().__init__(settings)
        self.colour_button = (180, 180, 0)
        self.colour_button_marked = (180, 0, 120)
        self.colour_button_chosen = (0, 50, 200)

    def buttons(self):
        button_setup = b.ButtonSetup(self.x, self.y, rows=5, columns=9, x_margin=0)
        survive_text = b.Button(button_setup.position(row=1, column=1, column_size=9),
                                self.screen_fill, 'When cell survive')

        survive_buttons = []
        for i in range(9):
            survive_buttons.append(b.Button(button_setup.position(row=2, column=i + 1), self.colour_button, '{}'.format(i)))

        alive_text = b.Button(button_setup.position(row=3, column=1, column_size=9),
                              self.screen_fill, 'When cell is born')

        alive_buttons = []
        for j in range(9):
            alive_buttons.append(b.Button(button_setup.position(row=4, column=j + 1), self.colour_button, '{}'.format(j)))

        back_button = b.Button(button_setup.position(row=5, column=1, column_size=9), self.colour_button, 'back')

        buttons = [survive_text, survive_buttons, alive_text, alive_buttons, back_button]
        return buttons

    def events(self, event, pos, buttons):
        survive_buttons = buttons[1]
        alive_buttons = buttons[3]
        back_button = buttons[4]

        for x in range(len(survive_buttons)):
            if x in self.settings[4][0]:
                survive_buttons[x].colour = self.colour_button_chosen
        for y in range(len(alive_buttons)):
            if y in self.settings[4][1]:
                alive_buttons[y].colour = self.colour_button_chosen

        run = True

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_button.marked(pos):
                s.Settings(self.settings).run()
                run = False

            for i in range(len(survive_buttons)):
                if survive_buttons[i].marked(pos):
                    if i in self.settings[4][0]:
                        self.settings[4][0].remove(i)
                    else:
                        self.settings[4][0].append(i)

            for j in range(len(alive_buttons)):
                if alive_buttons[j].marked(pos):
                    if j in self.settings[4][1]:
                        self.settings[4][1].remove(j)
                        alive_buttons[j].colour = self.colour_button
                    else:
                        self.settings[4][1].append(j)
                        alive_buttons[j].colour = self.colour_button_chosen

        if event.type == pygame.MOUSEMOTION:
            back_button.colour = self.colour_button
            if back_button.marked(pos):
                back_button.colour = self.colour_button_marked

            for k in range(len(survive_buttons)):
                if k not in self.settings[4][0]:
                    survive_buttons[k].colour = self.colour_button
                if survive_buttons[k].marked(pos):
                    survive_buttons[k].colour = self.colour_button_marked

            for l in range(len(alive_buttons)):
                if l not in self.settings[4][1]:
                    alive_buttons[l].colour = self.colour_button
                if alive_buttons[l].marked(pos):
                    alive_buttons[l].colour = self.colour_button_marked

        return run
