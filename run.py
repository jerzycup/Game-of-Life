from menu import Menu
import pygame

pygame.init()

init_settings = [(800, 600), 20, True, True, [[2, 3], [3]]]

menu = Menu(init_settings)
menu.run()

