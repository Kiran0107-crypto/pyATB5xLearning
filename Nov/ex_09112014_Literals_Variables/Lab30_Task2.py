# Nov 9th Task 2
# Take 2 input from the user
# Print the Quotient and Remainder
# 15 -> num1
# 2 ->num2

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

# First method

Quotient1 = num1 // num2
print(f"Quotient is (Q): -> {Quotient1}")

Remainder1 = num1 % num2
print(f"Remainder is (R): ->{Remainder1}")

# Second method
num3 = int(input("Enter third number"))
num4 = int(input("Enter fourth number"))

Quotient2, Remainder2 = divmod(num3,num4)
print(f"Quotient & Remainder are ->{Quotient2} {Remainder2}")
