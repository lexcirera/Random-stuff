import random

def approximate_pi(num_points):
    # Keep track of the number of points that fall within the circle
    num_in_circle = 0

    # Simulate the specified number of points
    for i in range(num_points):
        # Generate random x and y coordinates in the range [-1, 1]
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Use the Pythagorean theorem to determine whether the point falls within the circle
        if (x**2 + y**2) <= 1:
            num_in_circle += 1

    # Use the ratio of points within the circle to the total number of points to approximate pi
    approximation = (4 * num_in_circle) / num_points
    return approximation


# Test the approximate_pi function
print(approximate_pi(1000)) # 3.1~
print(approximate_pi(10000)) # 3.13~
print(approximate_pi(100000)) # 3.14~

