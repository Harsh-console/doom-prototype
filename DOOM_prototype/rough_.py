import pygame
import math

# === Constants ===
SCREEN_SIZE = (1200, 600)
RADIUS = 3
TILE = 20
VEL = 1
ANGLE = 0
NUM_RAYS = 300  # Start value
MAX_NUM_RAYS = 400
MIN_NUM_RAYS = 50
STEP = 4
MAX_DEPTH = 250 // STEP
FOV = math.pi / 3
STEP_SCREEN = SCREEN_SIZE[0] // NUM_RAYS
projection_scaling_factor = 2500
h, H = 1, 2  # Player height, wall height

# === Pygame Init ===
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

# === Map ===
MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1], 
    [1, 0, 0, 0, 0, 1, 0, 1], 
    [1, 0, 0, 0, 0, 0, 0, 1], 
    [1, 0, 0, 0, 1, 1, 1, 1], 
    [1, 1, 0, 0, 0, 0, 0, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1], 
]

# === Player ===
player_surface = pygame.Surface((2*RADIUS, 2*RADIUS))
player_surface.set_colorkey((0, 0, 0))  # Make background transparent
player_rect = player_surface.get_rect(topleft=(25, 25))


# === Helper Functions ===
def can_move(x, y):
    corners = [
        (x, y),
        (x + player_rect.width, y),
        (x, y + player_rect.height),
        (x + player_rect.width, y + player_rect.height),
    ]
    for cx, cy in corners:
        map_x = int(cx // TILE)
        map_y = int(cy // TILE)
        if not (0 <= map_x < len(MAP[0]) and 0 <= map_y < len(MAP)):
            return False
        if MAP[map_y][map_x] == 1:
            return False
    return True


# === Game Loop ===
while True:
    screen.fill((0, 0, 0))
    pygame.display.set_caption(str(round(clock.get_fps(), 2)))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # === Map Drawing ===
    for y, row in enumerate(MAP):
        for x, val in enumerate(row):
            if val:
                pygame.draw.rect(screen, "white", pygame.Rect(x*TILE, y*TILE, TILE, TILE))

    # === Player Drawing ===
    player_surface.fill((0, 0, 0))  # Clear old frame
    pygame.draw.circle(player_surface, "red", (RADIUS, RADIUS), RADIUS)
    screen.blit(player_surface, player_rect)

    # === Movement ===
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and can_move(player_rect.x, player_rect.y - VEL):
        player_rect.y -= VEL
    if keys[pygame.K_DOWN] and can_move(player_rect.x, player_rect.y + VEL):
        player_rect.y += VEL
    if keys[pygame.K_LEFT] and can_move(player_rect.x - VEL, player_rect.y):
        player_rect.x -= VEL
    if keys[pygame.K_RIGHT] and can_move(player_rect.x + VEL, player_rect.y):
        player_rect.x += VEL
    if keys[pygame.K_a]:
        ANGLE -= 0.03
    if keys[pygame.K_d]:
        ANGLE += 0.03

    # === Precompute angles and directions ===
    angle_offset = -FOV / 2
    angle_step = FOV / NUM_RAYS
    cos_sin_table = [
        (math.cos(ANGLE + angle_offset + i * angle_step),
         math.sin(ANGLE + angle_offset + i * angle_step))
        for i in range(NUM_RAYS)
    ]

    # === Raycasting ===
    for i, (cos_a, sin_a) in enumerate(cos_sin_table):
        dx = STEP * cos_a
        dy = STEP * sin_a
        ray_x, ray_y = player_rect.center
        d = MAX_DEPTH * STEP
        hit_wall = False

        for depth in range(MAX_DEPTH):
            ray_x += dx
            ray_y += dy
            map_x = int(ray_x // TILE)
            map_y = int(ray_y // TILE)

            if not (0 <= map_x < len(MAP[0]) and 0 <= map_y < len(MAP)):
                break
            if MAP[map_y][map_x]:
                d = depth * STEP
                hit_wall = True
                break

        # Optionally draw ray (debug)
        # if i % 10 == 0:
        #     pygame.draw.line(screen, "lightblue", player_rect.center, (ray_x, ray_y))

        # Wall projection
        x_screen = i * STEP_SCREEN
        if d == 0: d = 1  # Avoid div by zero
        start_y = SCREEN_SIZE[1] / 2 - ((H - h) / d) * projection_scaling_factor
        end_y = SCREEN_SIZE[1] / 2 + (H / d) * projection_scaling_factor
        pygame.draw.line(screen, "white", (x_screen, start_y), (x_screen, end_y))

    # === Dynamic Ray Adjustment ===
    fps_now = clock.get_fps()
    if fps_now < 40 and NUM_RAYS > MIN_NUM_RAYS:
        NUM_RAYS -= 10
        STEP_SCREEN = SCREEN_SIZE[0] // NUM_RAYS
    elif fps_now > 55 and NUM_RAYS < MAX_NUM_RAYS:
        NUM_RAYS += 10
        STEP_SCREEN = SCREEN_SIZE[0] // NUM_RAYS

    # === Frame Update ===
    clock.tick(60)
    pygame.display.update()
