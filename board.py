from cell import Cell


class Board(object):
    """
    Class for board logic
    """

    play_field = []
    x_count = None
    y_count = None

    def __init__(self, x_count, y_count):
        self.play_field = []
        self.x_count = x_count
        self.y_count = y_count

        # Matrix creation
        for i in range(self.x_count):
            self.play_field.append([])
        for field in self.play_field:
            for i in range(self.y_count):
                field.append(Cell())

    def clear(self):
        self.play_field = []
        for i in range(self.x_count):
            self.play_field.append([])
        for field in self.play_field:
            for i in range(self.y_count):
                field.append(Cell())
