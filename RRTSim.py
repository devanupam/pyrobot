import pygame
from RRTBase import RRTCore 
from MapEnvironment import MapEnvDraw, MapEnvSettings
from Obstacles import Obstacles
from RandomSampling import MapNodes

# Draw the map with obstacles

def main():
    start = (50,50)
    goal = (1800,1000)
    map_dims = (2000, 2200)
    obstacles_dims = (100,100)
    obstacles_num = 50

    # Initialize pygame, RRTMap, and RRTGraph
    pygame.init()

    rrtmap = MapEnvDraw(start, goal, map_dims, 'RRT path planning Simulation', MapEnvSettings.white)
    obstacles = Obstacles(map_dims, obstacles_dims, obstacles_num)
    obstaclesList = obstacles.makeObstacles(start, goal)

    # Draw map
    rrtmap.drawMap(obstaclesList)

    # map_nodes = MapNodes(map_dims, obstaclesList)
    rrtCore = RRTCore(start, goal, map_dims, obstaclesList)
    

    # Update display and wait for user to close window
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # map_nodes.addNode()
        rrtCore.addEdge()
        rrtmap.drawNodes(rrtCore.tree_nodes)
        rrtmap.drawEdges(rrtCore.tree_nodes)
        pygame.display.flip()

if __name__ == '__main__':
    main()


