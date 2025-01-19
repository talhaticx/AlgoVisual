import pygame as pg

class _GUI(object):
    """
    A reusable GUI class built using Pygame.

    This class provides a simple framework for creating graphical user interfaces
    using the Pygame library. It is designed to be reusable, allowing users to
    customize the `update`, `draw`, and `handle_events` methods to suit specific
    application requirements.

    Methods:
        run(): Starts the main loop of the GUI.
        update(): Placeholder for updating application state. Should be overridden in subclasses.
        draw(): Renders content on the screen. Can be customized in subclasses.
        handle_events(): Handles user input and events. Can be extended in subclasses.
        _exit_method(): Processes quit and escape key events to exit the application.
    """

    def __init__(self):
        pg.init()
        info = pg.display.Info()
        screen_width = info.current_w
        screen_height = info.current_h
        (self.width, self.height) = screen_width*0.7, screen_height*0.7
        
        self.DIMENSIONS = [self.width, self.height]
        
        self.screen = pg.display.set_mode((self.width, self.height), pg.RESIZABLE)
        pg.display.set_caption("Simple GUI")
        self.font = pg.font.Font(None, 32)
        self.clock = pg.time.Clock()
        self.running = True
        
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
            
    def update(self):
        pass
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        text = self.font.render("Hello, World!", True, (255, 255, 255))
        self.screen.blit(text, [int(x/2) for x in self.DIMENSIONS])
        pg.display.flip()
        
    def handle_events(self):
        self._exit_method()
        
    def _exit_method(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
