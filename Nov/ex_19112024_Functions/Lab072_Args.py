def print_multi_arguments(*args):
    for i in args:
        print(i)


print_multi_arguments("Kiran")
print_multi_arguments("Kiran", "Bhan", "Singh")
print_multi_arguments("Kiran",10, True, False, 10.5, "Bhan", "Singh")