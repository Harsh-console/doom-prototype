import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
fps = 60
text_color = (64,64,64)
box_color = "#c0e8ec"
plyr_gravity = 0
game_Active = True
score = 0
score_list = [0]

sky_surface = pygame.image.load("sky.png").convert()
ground_surface = pygame.image.load("ground.png").convert()
snail_surface = pygame.image.load("snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (800,300))
plyr_surf = pygame.image.load('player_walk_1.png').convert_alpha()
plyr_rect = plyr_surf.get_rect(midbottom = (60,280))
text_font = pygame.font.Font(None, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_Active:
            if event.type == pygame.KEYDOWN:
                if plyr_rect.bottom >= 300:
                    if event.key == pygame.K_SPACE:
                        plyr_gravity = -15
            if event.type == pygame.MOUSEBUTTONDOWN:
                if plyr_rect.bottom >= 300:
                    if plyr_rect.collidepoint(pygame.mouse.get_pos()):
                        plyr_gravity = -15
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_Active = True
                    snail_rect.left = 800
                    score = 0

    if game_Active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        screen.blit(snail_surface,snail_rect)
        score_Surface = text_font.render("High Score : " + str(max(score_list)) +  " Score : " + str(score),True, text_color)
        score_rect = score_Surface.get_rect(topleft = (200,10))
        pygame.draw.rect(screen,box_color, score_rect)
        pygame.draw.rect(screen,box_color, score_rect, width = 2)

        screen.blit(score_Surface,score_rect)
        
        snail_rect.x -= 9

        #player
        plyr_gravity += 0.8
        plyr_rect.y += plyr_gravity
        screen.blit(plyr_surf, plyr_rect)

        #collision
        if plyr_rect.colliderect(snail_rect):
            game_Active = False
            score_list.append(score)

        
        if snail_rect.left <= -100 :
            snail_rect.left = 800
            score += 1
        mouse_pos = pygame.mouse.get_pos()
        if plyr_rect.bottom >= 300:
            plyr_rect.bottom = 300
            plyr_gravity = 0
    
    else:
        screen.fill("Yellow")

    clock.tick(fps)
    pygame.display.update()


















'''
    #pygame.draw.line(screen, "Gold",(0,0),pygame.mouse.get_pos(), width = 7)
    #pygame.draw.ellipse(screen, "Blue", score_rect, width = 3)

    #plyr_rect.x += 2

    #pygame.display.set_caption(str(clock.get_fps()))

'''