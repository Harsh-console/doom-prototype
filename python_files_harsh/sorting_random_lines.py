import pygame
import random
RES = WIDTH, HEIGHT = 1200, 600
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
LINE_WIDTH = 3
FPS = 60
MIN_HEIGHT = 3
MAX_HEIGHT = HEIGHT
line_list = []
BASE_COORDINATE = HEIGHT
LINE_COLOR = 'White'
step = 0
for i in range(WIDTH // LINE_WIDTH):
    line_list.append(i*LINE_WIDTH)
RANDOM_HEIGHT = []
for i in range(len(line_list)):
    RANDOM_HEIGHT.append(random.randint(MIN_HEIGHT, MAX_HEIGHT))
def draw_random_lines(height_list):
    for i, x in enumerate(line_list):
        height = height_list[i]
        pygame.draw.line(screen, LINE_COLOR, (x, BASE_COORDINATE), (x, height))
#one_step_insortion_sort
def one_step_insertion_sort(lis):
    global step
    step+=1
    if step >= len(lis)-1:
        pygame.quit()
        exit()
    temp_num = lis[step]
    for j in range(1, step+1):
        k = step - j
        if lis[k] < temp_num:
            lis[k+1] = lis[k]
        if lis[k]  > temp_num:
            break
        lis[k] = temp_num
    return lis
while True:
    screen.fill('Black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    draw_random_lines(one_step_insertion_sort(RANDOM_HEIGHT))
    pygame.display.update()
    clock.tick(FPS)
    pygame.display.set_caption(f'FPS : {clock.get_fps():.1f}')