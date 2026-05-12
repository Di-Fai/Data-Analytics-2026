# Calculates the area of a circle using birthday day as the diameter
# Radius = Diameter / 2
# Area = π × radius**2

import math

# The diameter is the full distance across the circle.
# The radius is half of the diameter.
diameter = 14
radius = diameter / 2

# Calculate the area of the circle
area = math.pi * radius ** 2

# Display the result
print("The area of a circle with radius " + str(radius) + " is " + format(area, ".2f"))