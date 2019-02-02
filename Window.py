import pygame


class Window(object):

    def __init__(self, settings):
        '''
        :param settings: settings in form [size of the window, size of cells, aging, rules]
        rules in form [[survive], [born]]
        '''
        super().__init__()
        self.settings = settings
        self.x = settings[0][0]
        self.y = settings[0][1]
        self.screen_fill = (100, 100, 100)

    def buttons(self):
        '''
        :return: buttons with positions
        '''
        return []

    def texts(self, text):
        '''
        :return: texts that will appear
        '''
        return []

    def events(self, event, pos, buttons):
        '''
        :param event: pygame event
        :param pos: position of mouse
        :param buttons: used buttons
        :return: action
        '''
        return False

    def run(self):
        '''
        :return: window that will run
        '''
        text = ['']

        buttons = self.buttons()

        run = True

        pygame.display.set_caption('Game of Life')
        screen = pygame.display.set_mode((self.x, self.y))

        while run:
            texts = self.texts(text)

            screen.fill(self.screen_fill)
            if buttons:
                for i in range(len(buttons)):
                    try:
                        buttons[i].draw(screen)
                    except AttributeError:
                        for j in range(len(buttons[i])):
                            buttons[i][j].draw(screen)

            if texts:
                for k in range(len(texts)):
                    screen.blit(texts[k][0], texts[k][1])

            pygame.display.update()

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                run = self.events(event, pos, buttons)
