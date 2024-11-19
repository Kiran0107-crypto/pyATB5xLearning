# Problem ->Find the Max between 3 Numbers

# Logic Building

# Step 1: User inputs - num1, num2, num3 ->integers
# Output -> int or string with max number

# Step 2 :logic> If else -1 condition

num1 = int((input("Enter the num1:\n")))
num2 = int((input("Enter the num2:\n")))
num3 = int((input("Enter the num3:\n")))

if num1 > num2 and num1 > num3:
    print(f"Max is: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"Max is: {num2}")
else:
    print(f"Max is: {num3}")
