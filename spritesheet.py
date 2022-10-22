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
    """Class for utilizing spritesheets
    """
    def __init__(self, sheet_image, frame_size, cols, rows=0, scale=0):
        """Initializes basic properties of the spritesheet.
        Args:
            sheet_image: path to the spritesheet.png.
            frame_size: a sequence of 2 ints representing the width and height
                        of a single frame/sprite.
            scale: (Optional) used to scale up the frame/sprite.
            cols & rows: Number of columns and rows in the sheet
        """
        self.sheet = pg.image.load(sheet_image).convert_alpha()
        self.frm_w = frame_size[0]
        self.frm_h = frame_size[1]
        self.scale = scale

        if cols:
            self.cols = cols
        if rows:
            self.rows = rows

    def get_frame(self, frame_num: int):
        """Returns a specific frame from the sheet.
        Calculates x y position using frame_num arguement.
        
        Note: First frame starts from 0.
        """
        # Calculate position of frame
        x = (frame_num%self.cols) * self.frm_w
        y = (frame_num//self.cols) * self.frm_h
        
        # Setup surface to blit frame on
        frame = pg.Surface((self.frm_w, self.frm_h)).convert()
        frame.blit(self.sheet, (0, 0), (x, y, self.frm_w, self.frm_h))
        frame.set_colorkey((0, 0, 0))
        
        # Scale up frame
        if self.scale:
            frame = pg.transform.scale(frame, 
                (self.frm_w*self.scale, self.frm_h*self.scale))

        return frame

    def image_at(self, rect):
        """Similar to get_frame method.
        Takes a pygame.Rect as an arguement to locate the frame.
        """
        x, y = rect.x, rect.y
        w, h = rect.width, rect.height

        # Setup surface and blit frame on it
        frame = pg.Surface((w, h)).convert()
        frame.blit(self.sheet, (0, 0), (x, y, w, h))
        frame.set_colorkey((0, 0, 0))

        # Scale up frame
        if self.scale:
            frame = pg.transform.scale(frame, (w*self.scale, h*self.scale))

        return frame

    def __iter__(self):
        """See __next__."""
        self.count = 0
        return self

    def __next__(self):
        """Iterates over each frame/sprite in the sheet and retruns it."""

        # End if count exceeds total frames
        if self.count > (self.cols-1):
            raise StopIteration
        
        frame_num = self.count
        self.count += 1
        
        return self.get_frame(frame_num)
        

walk_sheet = os.path.join('assets', '1_Enemies', '1', 'Walk.png')
sheet_1 = Spritesheet(walk_sheet, [48, 48], cols=6, scale=2)
frm_list = [frame for frame in sheet_1]
frame_0 = sheet_1.image_at(pg.Rect(48, 0, 48, 48))
print(help(Spritesheet))
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
        WIN.blit(frame_0, (0, 250))


        # Update display
        pg.display.flip()
        clock.tick(FPS)

    # Post loop
    pg.quit()
    sys.exit(0)

if __name__ == "__main__":
    main()
