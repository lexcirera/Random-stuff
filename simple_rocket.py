'''
This implementation uses a simple model to simulate the flight of a rocket. The Rocket class has properties for the rocket's position, velocity, angle, and angular velocity, as well as the thrust and time step of the simulation. The update() method uses these properties to update the position, velocity, and angle of the rocket at each time step of the simulation.
'''




import math

class Rocket:
    def __init__(self):
        # position and velocity
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0

        # angle and angular velocity
        self.angle = 0
        self.angular_v = 0

        # thrust
        self.thrust = 0

        # time step
        self.dt = 0.1

    def update(self):
        # update position
        self.x += self.vx * self.dt
        self.y += self.vy * self.dt

        # update velocity
        self.vx += math.cos(self.angle) * self.thrust * self.dt
        self.vy += math.sin(self.angle) * self.thrust * self.dt

        # update angle
        self.angle += self.angular_v * self.dt

rocket = Rocket()

# set initial values for position, velocity, and angle
rocket.x = 0
rocket.y = 0
rocket.vx = 10
rocket.vy = 20
rocket.angle = math.pi / 2

# set initial value for angular velocity and thrust
rocket.angular_v = 0.1
rocket.thrust = 0.1

# simulate flight for 100 time steps


for i in range(100):
    rocket.update()

    print("Position: ({}, {})".format(rocket.x, rocket.y))
    print("Velocity: ({}, {})".format(rocket.vx, rocket.vy))
    print("Angle: {}".format(rocket.angle))
    print("-------------------")
