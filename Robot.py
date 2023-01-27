import math
import pygame

class FourWheelRobot:
    def __init__(self, startPos, robotImg, width, follow=None):
        self.m2p = 3779.52 # from meters to pixels
        self.leader = False # Is this the leader
        self.follow = follow # whom to follow if not leader

        self.x, self.y = startPos # start position of robot
        # self.w = width
        self.theta = 0 # orientation, radians
        self.a = 20
        self.u = 30 # Linear vel, pixels/sec
        self.W = 0 # rotational vel, radians/sec

        self.trailSet = []

        self.img = pygame.image.load(robotImg) # skin image path
        self.rotated = self.img
        self.rect = self.rotated.get_rect(center=(self.x, self.y))

    #Distance between two points
    def dist(self, point1, point2):
        return math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)

    # Move the robot
    def move(self, dt, event=None):
        # Update position as a function of time using direct kinematics model
        self.x += (self.u * math.cos(self.theta) - self.a * math.sin(self.theta) * self.W) * dt
        self.y += (self.u * math.sin(self.theta) + self.a * math.cos(self.theta) * self.W) * dt
        self.theta += (self.W * dt)

        self.rotated = pygame.transform.rotate(self.img, math.degrees(-self.theta))
        self.rect = self.rotated.get_rect(center=(self.x, self.y))

        if self.leader:
            if event is not None:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.u += 1
                    if event.key == pygame.K_DOWN:
                        self.u -= 1
                    if event.key == pygame.K_LEFT:
                        self.W += 0.01
                    if event.key == pygame.K_RIGHT:
                        self.W -= 0.01
        else:
            self.following()
            
    # Update follower linear and rotational velocity using inverse kinematics
    def following(self):
        target = self.follow.trailSet[0]
        delta_x = target[0] - self.x
        delta_y = target[1] - self.y

        self.u = delta_x * math.cos(self.theta) + delta_y * math.sin(self.theta)
        self.W = (delta_y * math.cos(self.theta) - delta_x * math.sin(self.theta)) / self.a

    def draw(self, map):
        map.blit(self.rotated, self.rect)

    # Add new positions & draw trail line
    def trail(self, pos, map, color):
        for i in range(0, len(self.trailSet) - 1):
            pygame.draw.line(map, color, self.trailSet[i], self.trailSet[i+1])

        if self.trailSet.__sizeof__() > 5000:
            self.trailSet.pop(0)
        self.trailSet.append(pos)
