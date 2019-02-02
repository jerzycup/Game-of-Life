import pygame
from playground import Playground
from random import randint
from board import Board

x = 600
y = 600
cell_size = 1

board = Board(int(x/cell_size), int(y/cell_size))

counts = 0

for o in range(randint(0, int(y * y / cell_size ** 2))):
    board.play_field[randint(0, int(y / cell_size) - 1)][randint(0, int(y / cell_size) - 1)].alive = True

while counts != 10000:
    board = Playground(board).turn()
    counts += 1
    print(counts)
