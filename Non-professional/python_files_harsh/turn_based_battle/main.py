import pygame
from constants import *
from grid import *
from unit import *
from game import *
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
    def start_game(self):
        pass
    def check_events(self):
        global turn
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                moved = False
                px = self.player.rect.x // TILE
                py = self.player.rect.y // TILE
                if turn == 'player' and 0 < px < NUM_COLUMN and 0 < py < NUM_ROWS:
                    if (event.key == pygame.K_UP and can_move(px, py-1)): 
                        self.player.rect.y -= TILE
                    if (event.key == pygame.K_RIGHT and can_move(px+1, py)): 
                        self.player.rect.x += TILE
                        moved = True
                    if (event.key == pygame.K_DOWN and can_move(px, py+1)): 
                        self.player.rect.y += TILE 
                        moved = True
                    if (event.key == pygame.K_LEFT and can_move(px-1,py)): 
                        self.player.rect.x -= TILE 
                        moved = True
                if moved:
                    for enemy in  self.enemies[:]:
                        px = self.player.rect.x // TILE
                        py = self.player.rect.y // TILE
                        ex = enemy.rect.x // TILE
                        ey = enemy.rect.y // TILE
                        if abs(px - ex) + abs(py - ey) == 1:
                            self.enemies.remove(enemy)
                            break # kill 1 enemy at a time
                    turn = 'enemy'
                if turn == 'enemy':
                    self.handle_enemy_turns()
    def handle_enemy_turns(self):
        global turn
        for enemy in self.enemies:
            px = self.player.rect.x // TILE
            py = self.player.rect.y // TILE
            ex = enemy.rect.x // TILE
            ey = enemy.rect.y // TILE
            dx = px- ex
            dy = py - ey
            if abs(dx) + abs(dy) <=  1:
                self.player.health -= 1
                print(f'Player"s Health : {self.player.health}')
                if self.player.health <= 0:
                    print("GAME OVER!")
                    pygame.quit()
                    exit()
                continue
            if abs(dx) > abs(dy) : #prefer horizontal
                if dx > 0 and can_move(ex+1, ey):
                    enemy.rect.x += TILE
                if dx < 0 and can_move(ex-1, ey):
                    enemy.rect.x -= TILE
            else: #prefer vertical
                if dy > 0 and can_move(ex, ey+1):
                    enemy.rect.y += TILE
                if dy < 0 and can_move(ex, ey-1):
                    enemy.rect.y -= TILE
        turn = 'player'
    def call_(self):
        self.map = Map(self)
        self.player = Character(self, PLAYER_COLOR, (120,360), MAX_PLAYER_HEALTH, MAX_PLAYER_HEALTH)
        self.enemies = [
            Character(self, ENEMY_COLOR, (660, 300), MAX_ENEMY_HEALTH, MAX_ENEMY_HEALTH),
            Character(self, ENEMY_COLOR, (360, 480), MAX_ENEMY_HEALTH, MAX_ENEMY_HEALTH),
            Character(self, ENEMY_COLOR, (240, 240), MAX_ENEMY_HEALTH, MAX_ENEMY_HEALTH),
            Character(self, ENEMY_COLOR, (780, 120), MAX_ENEMY_HEALTH, MAX_ENEMY_HEALTH),
            Character(self, ENEMY_COLOR, (300, 180), MAX_ENEMY_HEALTH, MAX_ENEMY_HEALTH),
            Character(self, ENEMY_COLOR, (540, 420), MAX_ENEMY_HEALTH, MAX_ENEMY_HEALTH)
        ]
        self.player_controls = Player_Controls(self)
    def draw(self):
        self.screen.fill(BLACK)
        self.draw_map()
        self.draw_units()
    def draw_units(self):
        self.screen.blit(self.player.surface, self.player.rect)
        for enemy in self.enemies:
            self.screen.blit(enemy.surface, enemy.rect)
    def draw_map(self):
        for i, row in enumerate(MAP):
            for j, val in enumerate(row):
                if val:
                    pygame.draw.rect(self.screen, 'darkgray', (j*TILE, i*TILE, TILE, TILE), 2)
    def update(self):
        self.clock.tick(FPS)
        pygame.display.set_caption(f'FPS : {self.clock.get_fps():.1f}' + f' turn : {turn}')
        pygame.display.update()
    def run(self):
        self.start_game()
        self.call_()
        while True:
            self.check_events()
            self.draw()
            self.update()

if __name__ == "__main__":
    game = Game()
    game.run()