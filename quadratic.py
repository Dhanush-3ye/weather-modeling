# Function to read and solve quadratic equations from a file
import math
def solve_quadratic_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        # Split each line into a, b, c
        a, b, c = map(float, line.split())
        
        # Calculate discriminant
        discriminant = b**2 - 4*a*c
        
        if discriminant >= 0:
            # Calculate roots
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            print(f"Roots for {a}x^2 + {b}x + {c} = 0 are: {root1}, {root2}")
        else:
            print(f"No real roots for {a}x^2 + {b}x + {c} = 0")

# Call the function with the file name
solve_quadratic_from_file('input_data.txt')
