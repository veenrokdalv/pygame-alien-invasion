import pygame as pg


class App:
    """Class app.
    
    Manages all processes.
    """
    def __init__(self):
        """Initializing all settings."""
        
        # Settings window.
        self.width = 1422
        self.height = 800
        self.caption = 'alien invasion'
        self.background = pg.image.load('./images/App/Background.jpg')
        self.window = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption(self.caption)

        # Settings framerate.
        self.fps = 30
        self.framerate = pg.time.Clock().tick
    

    def close(self):
        """Ends the program."""

        pg.quit()
        quit()


    def event_handler(self):
        """Event handling program."""

        # Clicking on the cross.
        [self.close() for event in pg.event.get() if event.type == pg.QUIT]

        # Receiving the pressed keys on the keyboard.
        keys = pg.key.get_pressed()

        # Pressing ESCAPE.
        if keys[pg.K_ESCAPE]:
            self.close()

    
    def draw(self):
        self.window.blit(self.background, (0, 0))
        pg.display.update()


    def start(self):
        """Start of all processes of the appendix."""

        while True:
            self.event_handler()
            self.draw()
            self.framerate(self.fps)




