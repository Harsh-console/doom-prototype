import pygame
import math

# Setup screen 
pygame.init()
screen = pygame.display.set_mode((1200,600))
clock = pygame.time.Clock()

# Constants
ANGLE = 0
rand_num = 2000
pi = math.pi
fps = 60
RADIUS = 15  # Circle radius (was 30 in diameter, so radius = 15)

# Player
player_pos = [100, 100]  # Circle center

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player_pos[1] += 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_a]:
        ANGLE += 3

    # Draw circle as player
    pygame.draw.circle(screen, (255, 105, 180), player_pos, RADIUS)  # "Pink" in RGB

    # Draw line from center of circle
    pygame.draw.line(
        screen,
        (255, 255, 255),
        player_pos,
        (
            player_pos[0] + rand_num * math.cos(math.radians(ANGLE)),
            player_pos[1] + rand_num * math.sin(math.radians(ANGLE))
        )
    )

    clock.tick(fps)
    pygame.display.set_caption(str(clock.get_fps()))
    pygame.display.update()
