import math

class Rocket:
  def __init__(self, initial_position, initial_velocity):
    self.position = initial_position
    self.velocity = initial_velocity
    self.acceleration = 0
    self.trajectory = [initial_position]

  def update(self, time_delta):
    self.velocity += self.acceleration * time_delta
    self.position += self.velocity * time_delta
    self.trajectory.append(self.position)

  def launch(self, initial_acceleration):
    self.acceleration = initial_acceleration

  def simulate(self, time_delta, duration):
    for _ in range(int(duration / time_delta)):
      self.update(time_delta)

rocket = Rocket((0, 0), (0, 0))
rocket.launch(10)
rocket.simulate(0.1, 10)


import matplotlib.pyplot as plt

x = [p[0] for p in rocket.trajectory]
y = [p[1] for p in rocket.trajectory]

plt.plot(x, y)
plt.show()
