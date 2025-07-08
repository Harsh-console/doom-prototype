import pygame
import random

# --- Constants ---
RES = WIDTH, HEIGHT = 1200, 600
FPS = 60
SIDE = 30
VEL = 5  # Grid-aligned movement

FOOD_RADIUS = SIDE // 2
BLOCK_SEGMENTS = []  # List of Snake block instances
DIR = 5  # 0: game over, 1: up, 2: right, 3: down, 4: left, 5: stop

TAIL_COLOR = "White"
HEAD_COLOR = "Gold"
FOOD_COLOR = "Orange"
GAME_OVER = False

# --- Pygame Setup ---
pygame.init()
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

font_large = pygame.font.Font(None, 60)
font_small = pygame.font.Font(None, 40)

game_over_surface = font_large.render("GAME OVER!", True, 'White')
game_over_rect = game_over_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

restart_surface = font_small.render("RESTART SNAKE GAME", True, 'White')
restart_rect = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))

# --- Snake Block Class ---
class SnakeBlock:
    def __init__(self, pos):
        self.surface = pygame.Surface((SIDE, SIDE))
        self.rect = self.surface.get_rect(topleft=pos)
        BLOCK_SEGMENTS.append(self)

# --- Initial Setup ---
BLOCK_SEGMENTS.clear()
head = SnakeBlock((SIDE * 3, SIDE * 3))
history = []  # Stores head positions for tail to follow

food_surface = pygame.Surface((SIDE, SIDE), pygame.SRCALPHA)
food_rect = food_surface.get_rect(topleft=(SIDE * 5, SIDE * 5))

def place_food():
    food_rect.x = random.randrange(0, WIDTH, SIDE)
    food_rect.y = random.randrange(0, HEIGHT, SIDE)

place_food()

# --- Game Loop ---
while True:
    score = 0
    DIR = 5
    history = []

    while not GAME_OVER:
        screen.fill("Black")

        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and DIR != 3:
            DIR = 1
        if keys[pygame.K_RIGHT] and DIR != 4:
            DIR = 2
        if keys[pygame.K_DOWN] and DIR != 1:
            DIR = 3
        if keys[pygame.K_LEFT] and DIR != 2:
            DIR = 4

        # --- Movement ---
        if DIR in (1, 2, 3, 4):
            dx, dy = 0, 0
            if DIR == 1: dy = -VEL
            if DIR == 2: dx = VEL
            if DIR == 3: dy = VEL
            if DIR == 4: dx = -VEL
            head.rect.x += dx
            head.rect.y += dy

            # Store head position
            history.insert(0, head.rect.topleft)
            if len(history) > 1000:
                history.pop()

            # Move body segments to follow history
            for i in range(1, len(BLOCK_SEGMENTS)):
                index = i * (SIDE // VEL)
                if index < len(history):
                    BLOCK_SEGMENTS[i].rect.topleft = history[index]

        # --- Draw Snake ---
        for i, block in enumerate(BLOCK_SEGMENTS):
            block.surface.fill(HEAD_COLOR if i == 0 else TAIL_COLOR)
            screen.blit(block.surface, block.rect)

        # --- Check for Food Collision ---
        if head.rect.colliderect(food_rect):
            place_food()
            score += 1
            # Add new segment offscreen; it will follow
            new_tail = SnakeBlock((-SIDE, -SIDE))

        # --- Draw Food ---
        pygame.draw.circle(screen, FOOD_COLOR, food_rect.center, FOOD_RADIUS)

        # --- Check Boundaries ---
        if head.rect.left < 0 or head.rect.right > WIDTH or \
           head.rect.top < 0 or head.rect.bottom > HEIGHT:
            DIR = 0
            GAME_OVER = True
        for i in range(len(BLOCK_SEGMENTS)):
            if i!=0 and i!= 1:
                if BLOCK_SEGMENTS[0].rect.colliderect(BLOCK_SEGMENTS[i]):
                    DIR = 0
                    GAME_OVER = True

        pygame.display.update()
        pygame.display.set_caption(f'Snake | Score: {score} | FPS: {clock.get_fps():.1f}')
        clock.tick(FPS)

    # --- Game Over Screen ---
    screen.fill("Black")
    screen.blit(game_over_surface, game_over_rect)
    screen.blit(restart_surface, restart_rect)
    pygame.display.update()
    pygame.time.wait(1000)

    while GAME_OVER:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos):
                    # Reset game
                    BLOCK_SEGMENTS.clear()
                    head = SnakeBlock((SIDE * 3, SIDE * 3))
                    place_food()
                    history = []
                    GAME_OVER = False
                    score = 0
                    DIR = 5

        pygame.display.update()
