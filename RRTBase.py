# RRT implementation and visualization using pygame

import pygame
import MapEnvironment

class RRTMap:
    pass

class RRTCore:
    def __init__(self, start, goal, map_dimensions, obstacles):
        (x, y) = start
        self.start = start
        self.goal = goal
        self.goal_flag = False
        self.map_height, self.map_width = map_dimensions

        # Tree structure
        self.x = []
        self.y = []
        self.parent = []

        self.x.append(x)
        self.y.append(y)
        self.parent.append(0)

        # Initialize obstacles
        self.obstacles = obstacles

        # Goal state
        self.goal_state = None
        self.path = []

    def addNode(self):
        pass

    def addEdge(self):
        pass

    def removeNode(self):
        pass

    def removeEdge(self):
        pass

    def numNodes(self):
        pass

    def distance(self):
        pass

    def nearest(self):
        pass

    def isFree(self):
        pass

    def crossObstacle(self):
        pass

    def connect(self):
        pass

    def step(self):
        pass

    def pathToGoal(self):
        pass

    def getPathCoordinates(self):
        pass

    def bias(self):
        pass

    def expand(self):
        pass

    def cost(self):
        pass


