import pygame
screen = pygame.display.set_mode((1200,600))
clock = pygame.time.Clock()

man_surface = pygame.image.load('man.png')
man_rect = man_surface.get_rect(topleft = (500,300))

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(man_surface, man_rect)
    pygame.display.update()
    clock.tick(60)