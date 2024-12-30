# Get input values from the user
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
c = float(input("Enter value for c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

if discriminant >= 0:
    # Calculate two solutions
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Root 1: {root1}, Root 2: {root2}")
else:
    print("No real roots")
