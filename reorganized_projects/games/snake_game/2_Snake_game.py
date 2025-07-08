import pygame
import random

#constants
RES = WIDTH, HEIGHT = 1200, 600
FPS = 60
TILE = 30
FOOD_RADIUS = int(TILE / 2)
HEAD_COLOR = (0, 255, 180)        # Bright Neon Mint (Head)
TAIL_COLOR = (0, 120, 255)        # Bright Sky Blue (Tail)
FOOD_COLOR = (255, 20, 147)       # Neon Pink (Food)
BG_COLOR   = (10, 10, 30)         # Dark Blue-Black (Background)
LINE_COLOR = (40, 40, 60)         # Subtle Grid
BLOCK_SEGMENT = []
dir = 0 # 0:stop, 1: up, 2: right, 3: down, 4: left
history = [] # store snake head previous postions for tail to follow

def random_food_pos():
    x = random.randint(0, (WIDTH - TILE)//TILE)
    y = random.randint(0, (HEIGHT - TILE)//TILE)
    return x*TILE,y*TILE

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.frame_count = 0
        self.snake_speed = 5 # no. of frame after which snake move one tile
        self.score = 0
    def draw_map(self):
        for i in range(int(WIDTH/TILE)):
            pygame.draw.line(self.screen, LINE_COLOR, (i * TILE, 0), (i*TILE, HEIGHT))
        for i in range(int(HEIGHT/TILE)):
            pygame.draw.line(self.screen, LINE_COLOR, (0, i*TILE), (WIDTH, i*TILE))
    def start_game(self):
        self.screen.fill(BG_COLOR)
        #BLOCK_SEGMENT.clear()
        self.head = Snake(HEAD_COLOR, self, random_food_pos())
        self.food = Food(self)
    def check_events(self):
        global dir
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and dir != 3: dir = 1
        if keys[pygame.K_RIGHT] and dir != 4: dir = 2
        if keys[pygame.K_DOWN] and dir != 1: dir = 3
        if keys[pygame.K_LEFT] and dir != 2: dir = 4
    def draw(self):
        self.screen.fill(BG_COLOR)
        for block in BLOCK_SEGMENT:
            block.draw()
        self.food.draw()
    def update(self):
        self.clock.tick(FPS)
        pygame.display.update()
        pygame.display.set_caption(f'FPS : {self.clock.get_fps() :.1f} ' + f', Score : {self.score}')
    def move_snake(self):
        global history
        self.frame_count += 1
        if self.frame_count % self.snake_speed != 0:
            return 1
        head = BLOCK_SEGMENT[0].rect
        history.append(head.topleft)
        if len(history) > 1000:
            history.pop(0)
        if dir == 1: head.y -= TILE
        if dir == 2: head.x += TILE
        if dir == 3: head.y += TILE
        if dir == 4: head.x -= TILE
        if head.x <= 0: head.x = 0
        if head.y <= 0: head.y = 0
        if head.x >= WIDTH - TILE : head.x = WIDTH - TILE
        if head.y >= HEIGHT - TILE : head.y = HEIGHT - TILE
    def snake_breakfast(self):
        if self.head.rect.colliderect(self.food.rect):
            self.food.move_food()
            self.score += 1
            last = BLOCK_SEGMENT[-1]
            last_pos_x, last_pos_y = last.rect.topleft
            if dir == 1: last_pos_y += TILE
            if dir == 2: last_pos_x -= TILE
            if dir == 3: last_pos_y -= TILE
            if dir == 4: last_pos_x += TILE
            new_tail = Snake(TAIL_COLOR, game, (last_pos_x, last_pos_y))
    def move_snake_tail(self):
        for i in range(1, len(BLOCK_SEGMENT)):
            #BLOCK_SEGMENT[i].rect.topleft = BLOCK_SEGMENT[i-1].rect.topleft
            delay = i*1
            if len(history) > delay:
                BLOCK_SEGMENT[i].rect.topleft = history[-delay-1]

    def run(self):
        self.start_game()
        while True:
            self.check_events()
            self.move_snake()
            self.move_snake_tail()
            self.update()
            self.draw()
            self.draw_map()
            self.snake_breakfast()

class Snake:
    def __init__(self, color, game, init_pos):
        self.game = game
        self.surface = pygame.Surface((TILE, TILE))
        self.init_pos = init_pos
        self.rect = self.surface.get_rect(topleft = self.init_pos)
        self.color = color
        BLOCK_SEGMENT.append(self)
    def draw(self):
        self.surface.fill(self.color)
        self.game.screen.blit(self.surface, self.rect)

class Food:
    def __init__(self, game):
        self.game = game
        self.surface= pygame.Surface((TILE, TILE))
        self.rect = self.surface.get_rect(topleft = random_food_pos())
    def draw(self):
        self.surface.fill(FOOD_COLOR)
        self.game.screen.blit(self.surface, self.rect)
    def move_food(self):
        self.rect.topleft = random_food_pos()

if  __name__ == "__main__":
    game = Game()
    game.run()