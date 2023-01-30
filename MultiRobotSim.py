import MapEnvironment
import pygame
import Robot


# Run the simulation for each robot
def multi_robot_simulation(Robot, dt, environment, event=None):
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
    environment = MapEnvironment.MapEnvSettings(dims, 'Multi Robot Simulation')

    #Create robots
    robots_followers = []
    robot_leader = Robot.FourWheelRobot(start, r'assets/vehicles/4wheelRobot.png', 50)
    robot_leader.leader = True

    robot_follower1 = Robot.FourWheelRobot((start[0] - 200, start[1]), r'assets/vehicles/4wheelRobot.png', robot_leader)
    robots_followers.append(robot_follower1)

    robot_follower2 = Robot.FourWheelRobot((start[0] - 400, start[1]), r'assets/vehicles/4wheelRobot.png', robot_follower1)
    robots_followers.append(robot_follower2)

    #animation loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Call the simulation for each robot
        multi_robot_simulation(robot_leader, dt, environment, event)

        for robot in robots_followers:
            multi_robot_simulation(robot, dt, environment)

        pygame.display.flip()
        environment.map.fill(environment.black)

        #difference between current time and last time
        dt = (pygame.time.get_ticks() - lastTime) / 1000 #seconds
        lastTime = pygame.time.get_ticks()
        iterations += 1


if __name__ == '__main__':
    main()