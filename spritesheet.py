import sys, os
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

# Spritesheet class
class Spritesheet():
    """Class for utilizing spritesheets"""
    def __init__(self, sheet_image, frame_size, scale):
        """Initialize the basic properties of the spritesheet.
        Args:
            sheet_image: path to the spritesheet.png.
            frame_size: a sequence of 2 ints representing the width and height
                        of a single frame in the sheet.
            scale: an int to which the frame will be scaled.
        """
        self.sheet = pg.image.load(sheet_image).convert_alpha()
        self.frame_w = frame_size[0]
        self.frame_h = frame_size[1]
        self.scale = scale

    def get_frame(self, frame):
        image = pg.Surface((self.frame_w, self.frame_h))
        
        image.blit(self.sheet, (0, 0), 
            (frame*self.frame_w, 0, self.frame_w, self.frame_h))
        
        image = pg.transform.scale(image, 
            (self.frame_w*self.scale, self.frame_h*self.scale))

        return image


walk_sheet = os.path.join('assets', '1_Enemies', '1', 'Walk.png')
sheet_1 = Spritesheet(walk_sheet, [48, 48], 2)
frame_0 = sheet_1.get_frame(5)

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
        WIN.blit(frame_0, (0, 150))


        # Update display
        pg.display.flip()
        clock.tick(FPS)


    # Post loop
    pg.quit()
    sys.exit(0)

if __name__ == "__main__":
    main()
