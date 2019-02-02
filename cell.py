class Cell(object):

    alive = None

    def __init__(self, alive=False):
        self.young_colour = [0, 200, 200]

        self.alive = alive
        self.age = 0

        self.colour = self.young_colour
        self.colour_step = [2, -2, -2]

    def aging(self):
        if self.age == 90:
            self.alive = False
            self.age = 0
            self.colour = self.young_colour

        if self.alive:
            for i in range(3):
                self.colour[i] += self.colour_step[i]

            self.age += 1
