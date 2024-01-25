from math import *

# Get user inputs
A = int(input("Please enter the value of A in Quadratic Eq.: "))
B = int(input("Please enter the value of B in Quadratic Eq.: "))
C = int(input("Please enter the value of C in Quadratic Eq.: "))

# Calculate the discriminant
discriminant = B**2 - 4*A*C

# Calculate the roots
if discriminant > 0:
    x1 = (-B + sqrt(discriminant)) / (2*A)
    x2 = (-B - sqrt(discriminant)) / (2*A)
    print(f"The roots are real and different: x1 = {x1}, x2 = {x2}")
elif discriminant == 0:
    x = -B / (2*A)
    print(f"The roots are real and equal: x = {x}")
else:
    real_part = -B / (2*A)
    imaginary_part = sqrt(-discriminant) / (2*A)
    print(f"The roots are complex and conjugate: x1 = {real_part} + {imaginary_part}i, x2 = {real_part} - {imaginary_part}i")
