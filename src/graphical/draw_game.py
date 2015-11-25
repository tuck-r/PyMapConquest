import pygame

WHITE = (255, 255, 255)

class DrawGame:
    def __init__(self, game_state):
        # Figure out what size each tile should be and the window size.
        map_size = game_state.get_map_size()
        tile_dims = 20
        window_size = (map_size * tile_dims, map_size * tile_dims)
        # Select a tile colour for each player.

        # Initialise drawing surface window.
        self.window_dimensions = window_size

        pygame.init()
        self.DISPLAYSURF = pygame.display.set_mode(self.window_dimensions)
        pygame.display.set_caption("PyMapConquest")

    def draw_game_state(self, game_state):
        tile_array = game_state.get_map_tile_array()
        for a_row in tile_array:
            for a_tile in a_row:
                coords = a_tile.get_coordinates()
                held_by = a_tile.get_is_owned_by()

    def update_screen(self, game_state):
        # Clear drawing surface.
        self.DISPLAYSURF.fill(WHITE)
        # Draw game state.
        self.draw_game_state(game_state)
        # Update screen.
        pygame.display.update()

    def quit_game(self):
        pygame.quit()
