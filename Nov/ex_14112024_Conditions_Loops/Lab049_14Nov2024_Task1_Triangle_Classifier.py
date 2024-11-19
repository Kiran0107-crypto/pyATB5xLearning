"""Triangle Classifier:

Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides,
determine if the triangle is equilateral (all sides are equal),
isosceles (exactly two sides are equal),
or scalene (no sides are equal).
Use an if-else statement to classify the triangle.
s1, s2, s3 → int

o/p →. iso, eq, scelene
"""

# Logic Building
# Step1: Figure out Input & Output:
# Input:3 sides(a, b, c) ->float
a = float(input("Enter Side1:\n"))
b = float(input("Enter Side2:\n"))
c = float(input("Enter Side3:\n"))
# Output: Triangle is Equilateral or Triangle is Isosceles or Triangle is Scalene

# Step2: Rough Logic:
# triangle is equilateral (all sides are equal) -> if a == b and a == c
# isosceles (exactly two sides are equal) ->
# if a == b:
# elif a == c
# elif b == c
# scalene (no sides are equal)
# a != b and a!=c and b!=c

if a == b:
    if a == c or b == c:
        print("Triangle is Equilateral")
        print(f"Sides: {a} {b} {c}")
    else:
        print("Triangle is Isosceles")
        print(f"Sides: {a} {b} {c}")
elif b == c:
    print("Triangle is Isosceles")
    print(f"Sides: {a} {b} {c}")
elif a == c:
    print("Triangle is Isosceles")
    print(f"Sides: {a} {b} {c}")
else:
    print("Triangle is Scalene")
    print(f"Sides: {a} {b} {c}")
