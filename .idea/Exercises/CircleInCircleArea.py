# Importing math lib not write Pi value.
import math
import sys

# Validating input if input will be a string it will print "Oops, it is not a valid number! Please run again."
try:
    R1 = float(input("Please enter your inner radius: "))
    area1 = math.pi + R1 ** 2
    print("Area of you Inner Circle is: ",round(area1,2),"\n")
    print(" ")
except ValueError:
    print("Oops, it is not a valid number! Please run again.")
    sys.exit()

try:
    R2 = float(input("Please enter your middle radius: "))
    area2 = math.pi + R2 ** 2
    print("Area of you Middle Circle is: ",round(area2,2),"\n")
except ValueError:
    print("Oops, it is not a valid number! Please run again.")
    sys.exit()

try:
    R3 = float(input("Please enter your outer radius: "))
    area3 = math.pi + R3 ** 2
    print("Area of you Outer Circle is: ",round(area3,2),"\n")
except ValueError:
    print("Oops, it is not a valid number! Please run again.")
    sys.exit()

blueArea = area3 - area2
blackArea = area2 - area1
print("Blue-shaded area is: ",round(blueArea,2))
print("Black-shaded area is: ",round(blackArea,2))
print("Red-shaded area is: ", round(area1,2))