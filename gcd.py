def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a

# Test the gcd function
from random import randint
a=randint(0,1e7)
b=randint(0,1e7)
print("gcd of", a , "and ", b, " is ", gcd(a,b))
