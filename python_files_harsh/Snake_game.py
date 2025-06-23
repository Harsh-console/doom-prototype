import pygame
import random

#constants
RES =  WIDTH, HEIGHT = 1200, 600
FPS = 60
side = 30
food_radius = side/2
block_segment = [] # contain Snake class type of each block of snake
Direction_list = [0, 1, 2 ,3, 4] # 0: stop, 1: up, 2: right, 3: down, 4: left
dir = 0
VEL = 10
tail_color = "Blue"
head_color = "White"
food_color = "Orange"
GameOver = False
Score_list = []

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

class Snake():
    def __init__(self, pos, color):
        self.x, self.y = pos
        self.surface = pygame.Surface((side, side))
        self.surface.fill(color)
        self.rect = self.surface.get_rect(topleft = pos)
        block_segment.append(self)

head = Snake((50,50), head_color)

food_surface = pygame.Surface((2*food_radius, 2*food_radius))
food_rect = food_surface.get_rect(topleft = (150,200))

while __name__ == "__main__":
    while not GameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if dir == 0:
            pass
        if dir == 1:
            block_segment[0].rect.y -= VEL
        if dir == 2:
            block_segment[0].rect.x += VEL
        if dir == 3:
            block_segment[0].rect.y += VEL
        if dir == 4:
            block_segment[0].rect.x -= VEL

        #head_move
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and dir != 3:
            dir = 1
        if keys[pygame.K_RIGHT] and dir != 4:
            dir = 2
        if keys[pygame.K_DOWN] and dir != 1:
            dir = 3
        if keys[pygame.K_LEFT] and dir != 2:
            dir = 4
        
        if dir == 4 and block_segment[0].rect.x == 0:
            dir = 0
        if dir == 2 and block_segment[0].rect.x == WIDTH - side:
            dir = 0
        if dir == 1 and block_segment[0].rect.y == 0:
            dir = 0
        if dir == 3 and block_segment[0].rect.y == HEIGHT - side:
            dir = 0

        #movement and draw
        if len(block_segment) >= 2:
            for i in range(2, len(block_segment)):
                block_segment[i].center = block_segment[i-1].center
                screen.blit(block_segment[i].surface, block_segment[i].rect)
        screen.blit(block_segment[0].surface, block_segment[0].rect)

        # check it snake eat food
        if block_segment[0].rect.colliderect(food_rect):
            food_rect.x = random.randint(0, WIDTH - 2*int(food_radius))
            food_rect.y = random.randint(0, HEIGHT - 2*int(food_radius))

        #draw food
        pygame.draw.circle(screen , food_color, food_rect.center, food_radius)

        pygame.display.update()
        pygame.display.set_caption(f'FPS : {clock.get_fps() :.1f}')
        clock.tick(FPS)

        if dir == 0:
            GameOver = True
        screen.fill("Black")
    while GameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
