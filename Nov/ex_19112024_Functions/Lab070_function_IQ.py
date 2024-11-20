#Create a Program to sum of three numbers from user input,
#if user doesn't enter any number, use default as 100, 200, 300

def sum_of_three_num(num1=100, num2=200, num3=300):
    sum= num1+num2+num3
    return sum

result_default = sum_of_three_num()
print(result_default)

result2 = sum_of_three_num(10)
print(result2)

result3 = sum_of_three_num(10,20)
print(result3)

result4 = sum_of_three_num(10,20, 30)
print(result4)

num1= int(input("Enter first number:\n"))
num2= int(input("Enter first number:\n"))
num3= int(input("Enter first number:\n"))

result = sum_of_three_num(num1, num2, num3)
print(result)



