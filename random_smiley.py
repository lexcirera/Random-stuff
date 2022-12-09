# Import the Pygame library
import pygame

# Initialize the Pygame library
pygame.init()

# Set the dimensions of the window
width = 400
height = 400

# Create the window
window = pygame.display.set_mode((width, height))

# Set the title of the window
pygame.display.set_caption("Smiley Face")

# Define the colors
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

# Draw the smiley face
# Draw the head
pygame.draw.circle(window, yellow, (200, 200), 150)
# Draw the eyes
pygame.draw.circle(window, black, (150, 150), 20)
pygame.draw.circle(window, black, (250, 150), 20)
# Draw the mouth
pygame.draw.arc(window, black, (100, 150, 200, 200), 0, 3.14, 20)

# Update the window
pygame.display.flip()

# Wait for the user to close the window
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
