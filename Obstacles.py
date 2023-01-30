import random
import pygame

# Class for creation of obstacles in the map

class Obstacles:
    def __init__(self, map_dim, obstacles_dim, obstacles_num):
        self.map_height, self.map_width = map_dim
        self.obstacles_dimensions = obstacles_dim
        self.obstacles_num = obstacles_num
        self.obstacles = []

    def makeRandomRect(self):
        upper_left_x = random.randint(0, self.map_width)
        upper_left_y = random.randint(0, self.map_height)

        return (upper_left_x, upper_left_y)

    def makeObstacles(self, start_pos, goal_pos):
        obstacles = []
        for i in range(0, self.obstacles_num):
            rectangle = None
            startGoalCollision = True
            while startGoalCollision:
                upper = self.makeRandomRect()
                rectangle = pygame.Rect(upper, self.obstacles_dimensions)
                startGoalCollision = rectangle.collidepoint(start_pos) or rectangle.collidepoint(goal_pos)
            obstacles.append(rectangle)
        self.obstacles = obstacles.copy()
        return obstacles
