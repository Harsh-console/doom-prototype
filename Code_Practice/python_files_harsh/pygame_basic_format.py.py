import pygame as pg

class SoftwareRenderer():
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1200, 600
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.screen = pg.display.set_mode(self.RES)
        self.FPS = 60
        self.clock = pg.time.Clock()
    def draw(self):
        self.screen.fill("Darkslategray")
    def run(self):
        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(f'FPS : {str(self.clock.get_fps() // 10 * 10)}')
            self.clock.tick(self.FPS)
            pg.display.flip()

if __name__ == "__main__":
    app = SoftwareRenderer()
    app.run()