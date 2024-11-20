"""FizzBuzz Test:

Write a program that prints numbers from 1 to 100. However,
for multiples of 3, print "Fizz" instead of the number,
and for multiples of 5, print "Buzz."
For numbers that are multiples of both 3 and 5, print "FizzBuzz." ( for, if)"""

# Logic Building
# Step 1:
# Input -> User Input not required
# Output:
# Case 1: Print number if number is not multiple of 3 or 5 or both
# Case 2: Print "Fizz" instead of the number if number is multiple of 3
# Case 3: Print "Buzz" instead of the number if number is multiple of 5
# Case 4: Print "FizzBuzz" instead of the number if number is multiple of 3 and 5

# Step 2:
# Logic
for i in range(1,101):
    if i % 3 ==0  and i % 5 ==0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
