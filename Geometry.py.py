import math
#stashed
def circle_area(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius ** 2
