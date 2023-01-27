import Environment
import pygame
import Robot


# Run the simulation for each robot
def robot_simulation(Robot, dt, environment, event=None):
    Robot.move(dt, event=event)
    Robot.draw(environment.map)
    Robot.trail((Robot.x, Robot.y), environment.map, environment.yellow)

def main(args=None):

    #Main
    pygame.init()
    running = True
    iterations = 0
    dt = 0
    lastTime = pygame.time.get_ticks()

    start = (500,200)
    dims = (2400,1800)
    environment = Environment.Envir(dims)

    #Create robot
    robot = Robot.DiffDriveRobot(start, r'assets/vehicles/DiffDriveRobot.png', 50)

    #animation loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Call the simulation for each robot
        robot_simulation(robot, dt, environment, event)

        pygame.display.flip()
        environment.map.fill(environment.black)

        #difference between current time and last time
        dt = (pygame.time.get_ticks() - lastTime) / 1000 #seconds
        lastTime = pygame.time.get_ticks()
        iterations += 1


if __name__ == '__main__':
    main()