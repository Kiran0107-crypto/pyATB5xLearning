def Triangle_Classifier(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and a + c > b and b + c > a:
            if a == b == c:
                return "Equilateral"
            elif a == b or b == c or a == c:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            print("Not a Triangle")
    else:
        print("Not a valid Length")


side1 = float(input("Enter first side1:\n"))
side2 = float(input("Enter first side2:\n"))
side3 = float(input("Enter first side3:\n"))

result = Triangle_Classifier(side1, side2, side3)
print(f"The triangle is classified as: {result}")
