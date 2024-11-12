# Write a program to take the 2 user input
# then sum the number
# mul -> *
# div -> /

# Logic Building
# Step 1
# Figure out Input -> num1, num2 -> int
# Figure out Output -> sum -int, sub ->int, div ->float

num1 = int(input("Enter the num 1: "))
num2 = int(input("Enter the num 2: "))
print(type(num1))
print(type(num2))

# num1 = int(num1)
# num2= int(num2

# Step 2 | Rough Logic
# Sum +, -, /, *
#str ->int


# Step 3 -Actual Logic
Sum = num1 + num2
Sub = num1 - num2
Mul = num1 * num2
Div = num1 / num2

print("Sum is ->", Sum)
print("Sub is ->", Sub)
print("Mul is ->", Mul)
print("Div is ->", Div)

num3 = float(input("Enter the num 3: "))
num4 = float(input("Enter the num 2: "))

Sum2 = num3 + num4
Sub2 = num3 - num4
Mul2 = num3 * num4
Div2 = num3 / num4

print("Sum is ->", Sum2)
print("Sub is ->", Sub2)
print("Mul is ->", Mul2)
print("Div is ->", Div2)

# num1 -> 155
# num2 -> 5
