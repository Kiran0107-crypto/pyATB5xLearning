
#Write a Python program to calculate
#Area of Circle given its radius using formula
# '''area=pi * r^2 (Take pie as 3.14)

#Logic Building formula

# || Step1 ||
#Figure out the input and output
#input ->r ->data type ->float
#pi=3.14
#power ->pow or ** ->any
#o/p ->float -area, print area

# Step2
#Rough Logic ->area= 3.14 * pow(r,2)

#Step3
import math
radius = float(input("Enter the radius of the circle\n"))
print(radius)
area= 3.14 * pow(radius,2)
print("Area of the circle is ->", area)
print(f"Area of the circle is ((Area)) : {area}")
area1=(math.pi)*(radius**2)
print(f"Area of Circle= {area1:.3f}")