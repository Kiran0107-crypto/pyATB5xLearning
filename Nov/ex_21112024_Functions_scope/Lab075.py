pb_global_b = 12


def my_func():
    pb_a = 10
    print(pb_a)
    print(pb_global_b)


my_func()

# print(pb_a) ->pb_a is local to functions my_func(), hence can't be used outside function
print(pb_global_b)
