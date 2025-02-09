# Robert Howe
# M2PA 3
# Surface area and volume of right cylinder, given height and radius.
import math # Enables math functions

print("To compute the surface area and volume of a right cylinder, the height and radius are required.")
print("The area includes the curved surface and both ends.")
radius = float(input("Enter the radius of the cylinder: ")) # Don't forget to convert string to float
height = float(input("Enter the height of the cylinder: "))
units = input("Enter the units of measure: ")
area = (2 * math.pi * radius * height) + (2 * math.pi * radius ** 2) # Don't forget import math
volume = math.pi * radius ** 2 * height
print(f" area is: {area: .4f} {units}²") # exponent text is alt 0178
print(f" volume is: {volume: .4f} {units}³") # exponent text is alt 0179