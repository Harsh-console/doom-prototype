import pygame
import math

#constants
SCREEN_SIZE = (1200, 600)
RADIUS = 3
fps = 60
TILE = 20
VEL = 1
ANGLE = 0
NUM_RAYS = 100
pi = math.pi
FOV = pi / 3
RAYS_per_radian = FOV / NUM_RAYS
MAX_RAY_LENGTH = 130

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

while True:
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
    pygame.draw.circle(player_surface, "Red", (RADIUS, RADIUS), RADIUS)
    screen.blit(player_surface,player_rect)

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
        pygame.draw.line(screen, "Pink", player_rect.center, 
                        (player_rect.center[0] + MAX_RAY_LENGTH*math.cos(angle), player_rect.center[1] + MAX_RAY_LENGTH*math.sin(angle)))

    #pygame
    clock.tick(fps)
    pygame.display.update()