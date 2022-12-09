'''
program in python of a realistic rocket simulator which take into account a wider range of factors, such as air resistance, gravitational forces, and the effects of burning fuel.
'''


import math
import matplotlib.pyplot as plt

# Define constants
GRAVITY = 9.81  # m/s^2
AIR_RESISTANCE_COEFF = 0.47
FUEL_BURN_RATE = 0.2  # kg/s

# Define initial conditions
INIT_VELOCITY = 0  # m/s
INIT_MASS = 1000  # kg
INIT_ALTITUDE = 0  # m

# Define simulation parameters
TIME_STEP = 0.1  # s
SIM_DURATION = 60  # s

# Initialize storage lists
time_list = []
altitude_list = []
velocity_list = []
mass_list = []

# Initialize time, velocity, altitude, and mass
time = 0
velocity = INIT_VELOCITY
altitude = INIT_ALTITUDE
mass = INIT_MASS

# Run simulation
while time <= SIM_DURATION:

    # Compute air resistance
    air_resistance = AIR_RESISTANCE_COEFF * math.sqrt(velocity)

    # Compute gravitational force
    gravitational_force = GRAVITY * mass

    # Compute acceleration
    acceleration = (gravitational_force - air_resistance) / mass

    # Update velocity and altitude
    velocity += acceleration * TIME_STEP
    altitude += velocity * TIME_STEP

    # Update mass based on fuel burn rate
    mass -= FUEL_BURN_RATE * TIME_STEP

    # Append data to storage lists
    time_list.append(time)
    altitude_list.append(altitude)
    velocity_list.append(velocity)
    mass_list.append(mass)

    # Update time
    time += TIME_STEP

# Plot results
plt.figure()
plt.plot(time_list, altitude_list)
plt.xlabel('Time (s)')
plt.ylabel('Altitude (m)')
plt.figure()
plt.plot(time_list,mass_list)
plt.xlabel('Time (s)')
plt.ylabel('Mass (kg)')
plt.show()