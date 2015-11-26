import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLOURS = {(255, 0, 0), (0, 255, 0), (0, 0, 255)}

class DrawGame:
    def __init__(self, game_state):
        # Figure out what size each tile should be and the window size.
        self.map_size = game_state.get_map_size()
        self.tile_dims = 25
        self.window_height = self.map_size * self.tile_dims
        self.window_width = self.map_size * self.tile_dims * 2
        self.window_size = (self.window_width, self.window_height)
        # Select a tile colour for each player.
        self.player_colours = {}
        for a_player in game_state.get_player_ids():
            self.player_colours[a_player] = COLOURS.pop()
        self.player_colours[None] = WHITE

        # Initialise drawing surface window.
        self.window_dimensions = self.window_size

        pygame.init()
        self.DISPLAYSURF = pygame.display.set_mode(self.window_dimensions)
        pygame.display.set_caption("PyMapConquest")

    def draw_game_state(self, game_state):
        tile_array = game_state.get_map_tile_array()
        # Iterate through every tile to draw the game map.
        for a_row in tile_array:
            for a_tile in a_row:
                coords = a_tile.get_coordinates()
                held_by = a_tile.get_is_owned_by()
                # Draw background colour rectangle.
                rect_coords = (coords[0] * self.tile_dims, coords[1] * self.tile_dims, self.tile_dims, self.tile_dims)
                pygame.draw.rect(self.DISPLAYSURF, self.player_colours[held_by], rect_coords)
                # Draw resource numbers in the corners
                # Corners are: {Top Left: Food, Top Right: Wood, Bottom Left: Gold, Bottom Right: Metal}

        # Draw black lines to form a grid.
        for i in range(0, self.map_size + 1):
            start_point_vert = (i * self.tile_dims, 0)
            start_point_horz = (0, i * self.tile_dims)
            end_point_vert = (i * self.tile_dims, self.map_size * self.tile_dims)
            end_point_horz = (self.map_size * self.tile_dims, i * self.tile_dims)
            pygame.draw.line(self.DISPLAYSURF, BLACK, start_point_vert, end_point_vert, 1)
            pygame.draw.line(self.DISPLAYSURF, BLACK, start_point_horz, end_point_horz, 1)
        # TODO: Draw player status/resources.

    def update_screen(self, game_state):
        # Clear drawing surface.
        self.DISPLAYSURF.fill(WHITE)
        # Draw game state.
        self.draw_game_state(game_state)
        # Update screen.
        pygame.display.update()

    def quit_game(self):
        pygame.quit()
