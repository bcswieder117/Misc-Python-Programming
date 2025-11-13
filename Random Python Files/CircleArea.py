# Blaine Swieder
# Area of a Circle
# July 4th, 2025

import math

def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return area

# Example usage:
radius = float(input("Enter the radius of the circle: "))
area = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}")
