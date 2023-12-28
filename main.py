import pygame
from menu import MainMenu


def main():
    pygame.init()
    width, height = 700, 600
    screen = pygame.display.set_mode((width, height))
    program_menu = MainMenu(width, height, screen)
    program_menu.run()


if __name__ == "__main__":
    main()
