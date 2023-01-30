import pygame
from RRTBase import RRTCore 
from RRTBase import RRTMap
from MapEnvironment import MapEnvDraw, MapEnvSettings
from Obstacles import Obstacles

# Draw the map with obstacles

def main():
    start = (50,50)
    goal = (2000,1000)
    map_dims = (2400,1800)
    obstacles_dims = (100,100)
    obstacles_num = 50

    # Initialize pygame, RRTMap, and RRTGraph
    pygame.init()

    rrtmap = MapEnvDraw(start, goal, map_dims, 'RRT path planning Simulation', MapEnvSettings.white)
    obstacles = Obstacles(map_dims, obstacles_dims, obstacles_num)
    obstaclesList = obstacles.makeObstacles(start, goal)
    # rrtCore = RRTCore(start, goal, dims, obstacles)

    # Draw map
    rrtmap.drawMap(obstaclesList)

    # Update display and wait for user to close window
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

if __name__ == '__main__':
    main()


