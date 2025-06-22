import pygame
import math

#constants
SCREEN_SIZE = (1200, 600)
RADIUS = 3
fps = 60
TILE = 20
VEL = 1
ANGLE = 0
NUM_RAYS = 400
pi = math.pi
FOV = pi / 3
RAYS_per_radian = FOV / NUM_RAYS
MAX_RAY_LENGTH = 250
STEP = 4
MAX_DEPTH = 100
STEP_SCREEN = SCREEN_SIZE[0] // NUM_RAYS
VERTICAL_FOV = pi / 2
h = 1 # Player's height
H = 2 # Wall height
d = MAX_DEPTH # default depth
projection_scaling_factor = 2500

#pygame
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

# Map (1 = wall, 0 = empty space)
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
#player
player_surface = pygame.Surface((2*RADIUS,2*RADIUS))
player_rect = player_surface.get_rect(topleft = (25,25))

def can_move(x, y):
    corners = [
        (x, y),  # top-left
        (x + player_rect.width, y),  # top-right
        (x, y + player_rect.height),  # bottom-left
        (x + player_rect.width, y + player_rect.height),  # bottom-right
    ]
    for cx, cy in corners:
        map_x = cx // TILE
        map_y = cy // TILE
        if not (0 <= map_x < len(MAP[0]) and 0 <= map_y < len(MAP)):
            return False
        if MAP[map_y][map_x] == 1:
            return False
    return True

while True:
    ray_lis = []
    screen.fill((0,0,0))
    pygame.display.set_caption(str(clock.get_fps()))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()        

    #map
    for y, row in enumerate(MAP):
        for x, state in enumerate(row):
                if state:
                    tile_rect = pygame.Rect(x*TILE, y*TILE, TILE, TILE)
                    pygame.draw.rect(screen, "White", tile_rect)

    #player
    player_surface.fill((0,0,0))
    pygame.draw.circle(player_surface, "Red", (RADIUS, RADIUS), RADIUS)
    screen.blit(player_surface,player_rect)

    #move
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

    #draw field of View
    for i in range(NUM_RAYS):
        angle = ANGLE - FOV/2 + (FOV/NUM_RAYS)*i
        dx = STEP * math.cos(angle)
        dy = STEP * math.sin(angle)
        ray_x, ray_y = player_rect.center
        hit_wall = False
        for depth in range(MAX_DEPTH):
            ray_x += dx
            ray_y += dy
            map_ray_x = int(ray_x // TILE)
            map_ray_y = int(ray_y // TILE)
            if MAP[map_ray_y][map_ray_x]:
                #pygame.draw.line(screen, "Light Blue", player_rect.center, (ray_x, ray_y))
                
                hit_wall = True
                d = depth * STEP
                break
        if not hit_wall:
            #pygame.draw.line(screen, "Light Blue", player_rect.center, (ray_x, ray_y))
            d = MAX_DEPTH
        
        x_screen = i * STEP_SCREEN
        if d != 0:
            if H >= h:
                start_pos_screen_line = (x_screen,(SCREEN_SIZE[1] / 2) - ((H-h) / d ) * projection_scaling_factor )
                end_pos_screen_line = (x_screen, (SCREEN_SIZE[1] / 2) + (H / d) * projection_scaling_factor)
                pygame.draw.line(screen, "White", start_pos_screen_line, end_pos_screen_line)


    #pygame
    if clock.get_fps() < 45:
        NUM_RAYS = max(100, NUM_RAYS - 10)
    else:
        NUM_RAYS = min(300, NUM_RAYS + 10)
    clock.tick(fps)
    pygame.display.flip()
    pygame.display.update()