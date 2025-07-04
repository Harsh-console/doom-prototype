
"""
import threading
import time

lis = [2,1,3]

def sleep_method(num):
    time.sleep(num)
    print(num)

for num in lis:
    t = threading.Thread(target = sleep_method, args=(num, ))
    t.start()
"""
import pygame
import threading
import time
import random

RES = HEIGHT, WIDTH = 1200,600
GAP = 3
LINE_COLOR = (255, 255, 255)

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

x_lis = []
height_lis = []

for i in range(0, WIDTH//GAP):
    x_lis.append(i*GAP)

def random_list(lis, lis_edit):
    n = len(lis)
    for i in range(n):
        lis_edit.append(random.randint(0, HEIGHT))

random_list(x_lis, height_lis)

def draw_lines(height_lis):
    for i, x in enumerate(x_lis):
        pygame.draw.line(screen, LINE_COLOR, (x, HEIGHT), (x, height_lis[i]))

state = True
while state:
    pygame.display.update()
    draw_lines(height_lis)
    time.sleep(2)
    state = False

while True:
    screen.fill('Black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    draw_lines(height_lis)
    pygame.display.update()