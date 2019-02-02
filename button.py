import pygame


class Button(object):

    button_setup = []
    colour = None
    text = ''

    def __init__(self, button_setup, colour, text, text_colour=(0, 0, 0)):
        super().__init__()
        self.x = button_setup[0]
        self.y = button_setup[1]
        self.width = button_setup[2]
        self.height = button_setup[3]
        self.colour = colour
        self.text = text
        self.text_colour = text_colour

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height), 0)

        font = pygame.font.SysFont('arial', int(0.85 * self.height))
        text = font.render(self.text, 1, self.text_colour)
        screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y +
                           (self.height / 2 - text.get_height() / 2)))

    def marked(self, pos):

        if self.x + self.width > pos[0] > self.x and self.y + self.height > pos[1] > self.y:
            return True

        else:
            return False


class ButtonSetup(object):

    def __init__(self, x, y, rows=1, columns=1, y_margin=0.05, x_margin=0.05, screen_margins=0.05):
        """
        :param x: x size of window
        :param y: y size of window
        :param columns: total number of columns (default 1)
        :param rows: total number of rows (default 1)
        :param y_margin: y margin between buttons (default 0.05)
        :param x_margin: x margin between buttons (default 0.05)
        :param screen_margins: x and y margin from the screen (default 0.05)
        """

        self.x = x * (1 - 2 * screen_margins)
        self.y = y * (1 - 2 * screen_margins)
        self.columns = columns
        self.rows = rows
        self.y_margin = y_margin * self.x
        self.x_margin = x_margin * self.y
        self.screen_margin_x = screen_margins * x
        self.screen_margin_y = screen_margins * y

    def position(self, row=1, column=1, row_size=1, column_size=1):
        """
        :param column: column (default 1)
        :param row: row (default 1)
        :param row_size: size of button in rows (default 1)
        :param column_size: size of button in columns (default 1)
        :return: values for creating buttons in this row and column
        """

        button_width = (self.x - (self.columns - column_size) * self.x_margin) / (self.columns - column_size + 1)
        button_height = (self.y - (self.rows - row_size) * self.y_margin) / (self.rows - row_size + 1)

        x_pos = (column - 1) * (button_width + self.x_margin) + self.screen_margin_x
        y_pos = (row - 1) * (button_height + self.y_margin) + self.screen_margin_y

        return [x_pos, y_pos, button_width, button_height]
