#Task 3
#Problem to find the max between two ( 3,4) → 4

#Step1 ->Figure out input and output
#Input-> 2 Numbers
Num1= int(input("Enter first number:\n"))
Num2=int(input("Enter second number:\n"))
#Output ->Maximum among both numbers

#Step 2 ->Rough Logic
#Approach 1 -> Use ">" to compare both numbers
if Num1>=Num2:
    print(f"Max number is: {Num1}")
else:
    print(f"Max number is: {Num2}")
#Approach 2 -> Use max function
print("=================================")
Max= max(Num1,Num2)
print(f"Max number is: {Max}")