import pygame
import math
pygame.init()

# Screen and map setup
WIDTH, HEIGHT = 800, 600
HALF_HEIGHT = HEIGHT // 2
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
clock = pygame.time.Clock()

# Map (1 = wall, 0 = empty space)
MAP = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,1,0,1,1,0,1],
    [1,0,1,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,1,0,1,0,1],
    [1,0,1,1,0,1,0,0,0,1],
    [1,0,0,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1],
]

TILE = 80
MAP_WIDTH = len(MAP[0])
MAP_HEIGHT = len(MAP)

# Player setup
player_x, player_y = 150, 150
player_angle = 0
FOV = math.pi / 3
NUM_RAYS = 60
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
SCALE = WIDTH // NUM_RAYS

def can_move(x, y):
    map_x = int(x // TILE)
    map_y = int(y // TILE)
    return 0 <= map_x < MAP_WIDTH and 0 <= map_y < MAP_HEIGHT and MAP[map_y][map_x] == 0

def draw_enemies():
    pass  # optional: enemy rendering if needed

def ray_casting():
    start_angle = player_angle - FOV / 2
    sin_table = [math.sin(start_angle + ray * DELTA_ANGLE) for ray in range(NUM_RAYS)]
    cos_table = [math.cos(start_angle + ray * DELTA_ANGLE) for ray in range(NUM_RAYS)]

    for ray in range(NUM_RAYS):
        sin_a = sin_table[ray]
        cos_a = cos_table[ray]

        for depth in range(0, MAX_DEPTH, 10):
            target_x = player_x + depth * cos_a
            target_y = player_y + depth * sin_a

            map_x = int(target_x // TILE)
            map_y = int(target_y // TILE)

            if 0 <= map_x < MAP_WIDTH and 0 <= map_y < MAP_HEIGHT:
                if MAP[map_y][map_x]:
                    depth *= math.cos(player_angle - (start_angle + ray * DELTA_ANGLE))
                    proj_height = min(HEIGHT, (TILE * 300) / (depth + 0.0001))
                    shade = 255 / (1 + depth * depth * 0.0001)
                    color = (shade, shade, shade)
                    pygame.draw.rect(
                        screen, color,
                        (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height)
                    )
                    break

# Main game loop
running = True
while running:
    screen.fill((0, 0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player_angle -= 0.03
    if keys[pygame.K_RIGHT]: player_angle += 0.03

    move_speed = 3
    dx = math.cos(player_angle) * move_speed
    dy = math.sin(player_angle) * move_speed

    if keys[pygame.K_w]:
        if can_move(player_x + dx, player_y): player_x += dx
        if can_move(player_x, player_y + dy): player_y += dy
    if keys[pygame.K_s]:
        if can_move(player_x - dx, player_y): player_x -= dx
        if can_move(player_x, player_y - dy): player_y -= dy
    if keys[pygame.K_a]:
        if can_move(player_x + dy, player_y): player_x += dy
        if can_move(player_x, player_y - dx): player_y -= dx
    if keys[pygame.K_d]:
        if can_move(player_x - dy, player_y): player_x -= dy
        if can_move(player_x, player_y + dx): player_y += dx

    ray_casting()
    pygame.display.flip()
    pygame.display.set_caption(str(clock.get_fps()))
    clock.tick(90)

pygame.quit()
