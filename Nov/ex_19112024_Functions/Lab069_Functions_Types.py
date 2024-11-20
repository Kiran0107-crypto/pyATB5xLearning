# User defined
# 1. They can't return ->non return
# 2. They can return something
# 3. They have parameters
# 4.They don't have parameters/ arguments

# 1. They can't return ->non return
# No Returns Type and No Parameters

def greet():
    print("Hello")


greet()


# 2. Not return Type with Argument / Parameters
def greet_by_name(name):
    print("Hello,", name)


greet_by_name("Kiran")


# 3. No Return Type and with Default Argument
def say_hello_default_arg(name="Kiran"):  # positional argument
    print("Hello", name.upper())


say_hello_default_arg("Singh")
say_hello_default_arg()


def multiple_args(name1="A", name2="B"):
    print("Hello ->", name1, name2)


multiple_args()
multiple_args("Kiran")
multiple_args(name1="Kiran")
multiple_args(name1="Kiran", name2="Singh")
multiple_args(name2="Bhan")


# 4. Argument + Return Type

def sum_of_two(a, b):
    return a + b


result = sum_of_two(4, 5)
print(result)

print("==========================")


def sum_of_two_number_with_default(num1=100, num2=200):
    return num1 + num2

result_sum=sum_of_two_number_with_default()
print(result_sum)

result_sum=sum_of_two_number_with_default(20,30)
print(result_sum)
