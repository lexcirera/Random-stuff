# Import the random module
import random

# Define the random algorithm
def random_algorithm():
  # Generate a random integer between 1 and 10
  random_int = random.randint(1, 10)
  # Generate a random float between 0 and 1
  random_float = random.random()
  # Generate a random string of 5 characters
  random_string = ''.join(random.choices(string.ascii_letters, k=5))
  # Return the generated values
  return random_int, random_float, random_string

# Test the random algorithm
print(random_algorithm())
