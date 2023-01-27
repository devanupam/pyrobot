import pygame

class Envir:
    def __init__(self, dimensions):
        #Colors
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.red = (255,0,0)
        self.green = (0,255,0)
        self.blue = (0,0,255)
        self.yellow = (255,255,0)
        self.orange = (255,165,0)

        #Map dimensions
        self.width, self.height = dimensions
        pygame.display.set_caption('Multi Robot Simulation')
        self.map = pygame.display.set_mode(dimensions)

    def write_info(self):
        pass

    def robot_frame(self):
        pass
