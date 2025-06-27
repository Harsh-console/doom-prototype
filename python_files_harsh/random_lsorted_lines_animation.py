import pygame
import random
RES = WIDTH, HEIGHT = 1200, 600
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
LINE_WIDTH = 3
FPS = 3
MIN_HEIGHT = 3
MAX_HEIGHT = HEIGHT
line_list = []
BASE_COORDINATE = HEIGHT
LINE_COLOR = 'White'
for i in range(WIDTH // LINE_WIDTH):
    line_list.append(i*LINE_WIDTH)
RANDOM_HEIGHT = []
for i in range(len(line_list)):
    RANDOM_HEIGHT.append(random.randint(MIN_HEIGHT, MAX_HEIGHT))
def draw_random_lines(height_list):
    for i, x in enumerate(line_list):
        height = height_list[i]
        pygame.draw.line(screen, LINE_COLOR, (x, BASE_COORDINATE), (x, height))
#insetion sort
def sort_list(lis):
    for i in range(0,len(lis)):
        temp_num = lis[i]
        for j in range(1, i+1):
            k = i - j
            if lis[k] > temp_num:
                lis[k+1] = lis[k]
            if lis[k] <= temp_num:
                break
            lis[k] = temp_num
    return lis
def new_heights():
    temp_height_list = []
    for i in range(len(line_list)):
        temp_height_list.append(random.randint(MIN_HEIGHT, MAX_HEIGHT))
    return temp_height_list
while True:
    screen.fill('Black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    draw_random_lines(sort_list(RANDOM_HEIGHT))
    pygame.display.update()
    clock.tick(FPS)
    pygame.display.set_caption(f'FPS : {clock.get_fps():.1f}')
    #new RANDOM_HEIGHTS
    RANDOM_HEIGHT = []
    RANDOM_HEIGHT = new_heights()