import pygame
import MapEnvironment

class MapEnvSettings:
    #Colors
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    yellow = (255,255,0)
    orange = (255,165,0)
    grey = (128,128,128)

    def __init__(self, dimensions, caption, color=(0,0,0)):
        #Map dimensions
        self.width, self.height = dimensions
        pygame.display.set_caption(caption)
        self.map = pygame.display.set_mode(dimensions)
        self.map.fill(color)

    def write_info(self):
        pass


# Class to draw the map, obstacles and path
class MapEnvDraw:
    def __init__(self, start, goal, map_dimensions, caption, color) -> None:
        self.environment = MapEnvironment.MapEnvSettings(map_dimensions, caption, color)
        self.start = start
        self.goal = goal
        self.node_radius = 4
        self.node_thickness = 0
        self.edge_thickness = 0
        # self.obstacles = []

    def drawMap(self, obstacles):
        # Draw start and goal as circles
        pygame.draw.circle(self.environment.map, self.environment.green, self.start, self.node_radius + 10, self.node_thickness)
        pygame.draw.circle(self.environment.map, self.environment.red, self.goal, self.node_radius + 20, self.node_thickness)
        
        # Draw obstacles
        self.drawObstacles(obstacles)

    def drawNodes(self, map_nodes):
        for node in map_nodes.nodes:
            pygame.draw.circle(self.environment.map, self.environment.blue, (node.x, node.y), self.node_radius, self.node_thickness)

    def drawPath(self):
        pass

    def drawObstacles(self, obstacles):
        for obstacle in obstacles:
            pygame.draw.rect(self.environment.map, self.environment.grey, obstacle)
