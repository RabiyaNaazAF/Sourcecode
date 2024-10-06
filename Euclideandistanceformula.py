import math

def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Get user input for the two points
try:
    x1, y1 = map(float, input("Enter the coordinates of the first point (x1 y1): ").split())
    x2, y2 = map(float, input("Enter the coordinates of the second point (x2 y2): ").split())

    point1 = (x1, y1)
    point2 = (x2, y2)

    distance = calculate_distance(point1, point2)
    print(f"The shortest distance between {point1} and {point2} is {distance:.2f} units.")
except ValueError:
    print("Please enter valid coordinates.")
