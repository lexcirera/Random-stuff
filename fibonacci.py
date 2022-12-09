def fibonacci(n):
  # Check if the number is 0 or 1
  if n == 0:
    return []
  elif n == 1:
    return [0]

  # Calculate the previous two numbers in the sequence
  fibonacci_1 = fibonacci(n - 1)
  fibonacci_2 = fibonacci(n - 2)

  # Add the previous two numbers in the sequence and append the result to the list
  fibonacci_1.append(fibonacci_1[-1] + fibonacci_2[-1])

  # Return the list of Fibonacci numbers
  return fibonacci_1

# Test the fibonacci function
print(fibonacci(1)) # [0]
print(fibonacci(2)) # [0, 1]
print(fibonacci(3)) # [0, 1, 1]
print(fibonacci(4)) # [0, 1, 1, 2]
print(fibonacci(5)) # [0, 1, 1, 2, 3]
