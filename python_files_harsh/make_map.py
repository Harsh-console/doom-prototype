import pygame
import sys
import json

# Constants
TILE_SIZE = 30
MAP_WIDTH = 40
MAP_HEIGHT = 20
SCREEN_WIDTH = TILE_SIZE * MAP_WIDTH
SCREEN_HEIGHT = TILE_SIZE * MAP_HEIGHT
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
WALL_COLOR = (100, 100, 255)

# Initialize
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tile Map Editor")
clock = pygame.time.Clock()

# Map data (0 = empty, 1 = wall)
map_data = [[0 for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

def draw_grid():
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            rect = pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if map_data[y][x] == 1:
                pygame.draw.rect(screen, WALL_COLOR, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)

def save_map(filename="map.json"):
    with open(filename, "w") as f:
        json.dump(map_data, f)

def load_map(filename="map.json"):
    global map_data
    with open(filename, "r") as f:
        map_data = json.load(f)

# Main loop
running = True
while running:
    screen.fill(WHITE)
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_map()
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            tile_x = x // TILE_SIZE
            tile_y = y // TILE_SIZE
            if pygame.mouse.get_pressed()[0]:  # Left click = place
                map_data[tile_y][tile_x] = 1
            elif pygame.mouse.get_pressed()[2]:  # Right click = remove
                map_data[tile_y][tile_x] = 0

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                save_map()
                print("Map saved.")
            elif event.key == pygame.K_l:
                load_map()
                print("Map loaded.")

    pygame.display.flip()
    clock.tick(60)
