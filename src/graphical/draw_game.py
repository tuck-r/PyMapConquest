import pygame

class DrawGame:
    def __init__(self):
        self.window_dimensions = (600, 400)

        pygame.init()
        self.DISPLAYSURF = pygame.display.set_mode(self.window_dimensions)
        pygame.display.set_caption("PyMapConquest")
        self.update_screen()

    def update_screen(self):
        pygame.display.update()

    def quit_game(self):
        pygame.quit()
