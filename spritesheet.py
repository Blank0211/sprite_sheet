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

# Sprites
class Spritesheet():
    """Class for utilizing spritesheets"""
    def __init__(self, sheet_image, frame_size, scale=0, cols=0, rows=0):
        """Initialize the basic properties of the spritesheet.
        Args:
            sheet_image: path to the spritesheet.png.
            frame_size: a sequence of 2 ints representing the width and height
                        of a single frame.
            scale: (Optional) used to scale up the frame.
            cols / rows: Number of columns and rows in the sheet
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
        """Return the specified frame from the sheet.
        Note: Frame starts from 0.
        """
        frame = pg.Surface((self.frm_w, self.frm_h))
        frame.set_colorkey((0, 0, 0))
        
        # Blit frame on surface
        frame.blit(self.sheet, (0, 0), 
            (frame_num*self.frm_w, 0, self.frm_w, self.frm_h))
        
        # Scale up frame
        if self.scale:
            frame = pg.transform.scale(frame, 
                (self.frm_w*self.scale, self.frm_h*self.scale))

        return frame

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        # End if count exceeds total frames
        if self.count > (self.cols-1):
            raise StopIteration
        
        frame_num = self.count
        self.count += 1
        
        return self.get_frame(frame_num)


class Player(pg.sprite.Sprite):
    def __init__(self, size, pos, sheet_file, **sheet_args):
        super().__init__()
        # Animation & Frames
        if sheet_file:
            self.sheet = Spritesheet(sheet_file, **sheet_args) 
            self.frames = [frame for frame in self.sheet]
        self.current_frame = 0
        self.is_animate = False

        # Appearance & Body
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(topleft=pos)

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_d]:
            self.is_animate = True

        if self.is_animate:
            self.current_frame += 0.2
            
            if self.current_frame >= len(self.frames):
                self.current_frame = 0
                self.is_animate = False

            self.image = self.frames[int(self.current_frame)]


    def draw(self, win):
        win.blit(self.image, self.rect)


walk_sheet = os.path.join('assets', '1_Enemies', '1', 'Walk.png')
# sheet_1 = Spritesheet(walk_sheet, [48, 48], 2, cols=6)
p1 = Player([48, 48], [0, 250], walk_sheet, 
        frame_size=[48, 48], scale=2, cols=6)



# Game loop
def main():
    pg.init()
    running = True
    while running:
        # Handle events
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                running = False
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_d:
                    p1.is_animate = True

        # Update / Draw
        p1.update()

        WIN.fill(PURPLE)
        p1.draw(WIN)

        # Update display
        pg.display.flip()
        clock.tick(FPS)

    # Post loop
    pg.quit()
    sys.exit(0)

if __name__ == "__main__":
    main()
