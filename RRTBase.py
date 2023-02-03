# RRT implementation and visualization using pygame

import math
from RandomSampling import MapNodes, Node

class TreeNode(Node):
    def __init__(self, x, y, parent) -> None:
        super().__init__(x, y)
        self.parent = parent

class RRTCore(MapNodes):
    def __init__(self, start, goal, map_dimensions, obstacles):
        # Call super constructor
        super().__init__(map_dimensions, obstacles)
        (x, y) = start
        self.start = start
        self.goal = goal
        self.goal_flag = False
        self.map_height, self.map_width = map_dimensions
        self.max_distance = 50 # Maximum distance to expand tree

        # Tree structure
        # self.x = []
        # self.y = []
        # self.parent = []

        # self.x.append(x)
        # self.y.append(y)
        # self.parent.append(0)

        self.tree_nodes = []
        self.tree_nodes.append(TreeNode(x, y, None))

        # Initialize obstacles
        self.obstacles = obstacles

        # Goal state
        self.goal_state = None
        self.path = []

    def addNode(self):
        # Call super add node
        # node = super().addNode()
        pass


    def addEdge(self):
        node = super().addNode()
        if node is None:
            return
        # Get nearest node
        nearest_node = super().nearestNNodes(self.tree_nodes, node, 1)[0]

        # Check if node is in obstacle
        if super().crossObstacle(nearest_node, node):
            return
        
        # If distance is greater than max distance, then put the node at max distance
        if super().distance(nearest_node, node) > self.max_distance:
            # Get angle
            angle = math.atan2(node.y - nearest_node.y, node.x - nearest_node.x)
            node.x = nearest_node.x + self.max_distance * math.cos(angle)
            node.y = nearest_node.y + self.max_distance * math.sin(angle)
        
        # Add node to tree and make it child of nearest node
        self.tree_nodes.append(TreeNode(node.x, node.y, nearest_node))

    def removeNode(self):
        pass

    def removeEdge(self):
        pass

    def numNodes(self):
        pass

    # def distance(self):
    #     pass

    def nearest(self):
        pass

    # def isFree(self):
    #     pass

    # def crossObstacle(self):
    #     pass

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