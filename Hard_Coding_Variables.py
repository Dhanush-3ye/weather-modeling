import math

# Hard-coded values for the quadratic equation
a = 1
b = -3
c = 2

# Calculate the discriminant
discriminant = b**2 - 4*a*c

if discriminant >= 0:
    # Calculate two solutions
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Root 1: {root1}, Root 2: {root2}")
else:
    print("No real roots")
