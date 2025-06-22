import pygame
import math
pygame.init()

# Screen and map setup
WIDTH, HEIGHT = 800, 600
HALF_HEIGHT = HEIGHT // 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Map (1 = wall, 0 = empty space)
MAP = [
    [1,1,1,1,1,1],
    [1,0,0,0,0,1],
    [1,0,1,0,0,1],
    [1,0,0,0,0,1],
    [1,1,1,1,1,1],
]
TILE = 100  # Map cell size
MAP_WIDTH = len(MAP[0])
MAP_HEIGHT = len(MAP)

# Player
player_x = 150
player_y = 150
player_angle = 0
FOV = math.pi / 3
NUM_RAYS = 120
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
SCALE = WIDTH // NUM_RAYS

def draw_map_2d():
    for y, row in enumerate(MAP):
        for x, tile in enumerate(row):
            rect = pygame.Rect(x * TILE // 5, y * TILE // 5, TILE // 5, TILE // 5)
            color = (255, 255, 255) if tile else (30, 30, 30)
            pygame.draw.rect(screen, color, rect)

    pygame.draw.circle(screen, (255, 0, 0), (int(player_x // 5), int(player_y // 5)), 3)

enemies = [
    {'x': 300, 'y': 300, 'alive': True}
]

def draw_enemies():
    for enemy in enemies:
        if not enemy['alive']:
            continue
        dx = enemy['x'] - player_x
        dy = enemy['y'] - player_y
        distance = math.hypot(dx, dy)

        angle_to_enemy = math.atan2(dy, dx)
        relative_angle = angle_to_enemy - player_angle

        # Only draw if in FOV
        if -FOV / 2 < relative_angle < FOV / 2:
            proj_height = min(HEIGHT, (TILE * 300) / (distance + 0.0001))
            x_offset = int((relative_angle + FOV / 2) / DELTA_ANGLE) * SCALE
            pygame.draw.rect(
                screen, (255, 0, 0),
                (x_offset - proj_height // 4, HALF_HEIGHT - proj_height // 2, proj_height // 2, proj_height)
            )


def ray_casting():
    start_angle = player_angle - FOV / 2
    for ray in range(NUM_RAYS):
        angle = start_angle + ray * DELTA_ANGLE
        sin_a = math.sin(angle)
        cos_a = math.cos(angle)

        for depth in range(MAX_DEPTH):
            target_x = player_x + depth * cos_a
            target_y = player_y + depth * sin_a

            map_x = int(target_x // TILE)
            map_y = int(target_y // TILE)

            if 0 <= map_x < MAP_WIDTH and 0 <= map_y < MAP_HEIGHT:
                if MAP[map_y][map_x]:
                    # Wall hit
                    depth *= math.cos(player_angle - angle)  # fix fish-eye
                    proj_height = min(HEIGHT, (TILE * 300) / (depth + 0.0001))
                    color = 255 / (1 + depth * depth * 0.0001)
                    pygame.draw.rect(
                        screen,
                        (color, color, color),
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

    # Rotate
    if keys[pygame.K_LEFT]:
        player_angle -= 0.03
    if keys[pygame.K_RIGHT]:
        player_angle += 0.03

    # Move
    move_speed = 3
    dx = math.cos(player_angle) * move_speed
    dy = math.sin(player_angle) * move_speed

    # Check for wall at target tile position
    def can_move(x, y):
        map_x = int(x // TILE)
        map_y = int(y // TILE)
        if 0 <= map_x < MAP_WIDTH and 0 <= map_y < MAP_HEIGHT:
            return MAP[map_y][map_x] == 0
        return False

    # Forward
    if keys[pygame.K_w]:
        if can_move(player_x + dx, player_y):
            player_x += dx
        if can_move(player_x, player_y + dy):
            player_y += dy

    # Backward
    if keys[pygame.K_s]:
        if can_move(player_x - dx, player_y):
            player_x -= dx
        if can_move(player_x, player_y - dy):
            player_y -= dy

    # Strafe Left (A)
    if keys[pygame.K_a]:
        if can_move(player_x + dy, player_y):
            player_x += dy
        if can_move(player_x, player_y - dx):
            player_y -= dx

    # Strafe Right (D)
    if keys[pygame.K_d]:
        if can_move(player_x - dy, player_y):
            player_x -= dy
        if can_move(player_x, player_y + dx):
            player_y += dx

    ray_casting()
    draw_map_2d()

    pygame.display.flip()
    pygame.display.set_caption(str(clock.get_fps()))
    clock.tick(60)

pygame.quit()
