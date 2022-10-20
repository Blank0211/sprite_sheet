import sys
import pygame as pg

# Colors
PURPLE = pg.Color("#4f2356")
BLACK = pg.Color(0, 0, 0)
WHITE = pg.Color(255, 255, 255)

# General setup
width, height, = 790, 480
WIN = pg.display.set_mode((width, height))
pg.display.set_caption("Spritesheet")
clock = pg.time.Clock()
FPS = 60

# Images
walk_1 = pg.image.load("assets/1 Enemies/1/Walk.png").convert_alpha()
scale = 2
# walk_1 = pg.transform.scale(walk_1, (288*scale, 48*scale))


# Game loop
def main():
    pg.init()
    running = True
    while running:
        # Handle events
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                running = False

        # Update / Draw
        WIN.fill(PURPLE)
        WIN.blit(walk_1, (0, 200))


        # Update display
        pg.display.flip()
        clock.tick(FPS)


    # Post loop
    pg.quit()
    sys.exit(0)

if __name__ == "__main__":
    main()
