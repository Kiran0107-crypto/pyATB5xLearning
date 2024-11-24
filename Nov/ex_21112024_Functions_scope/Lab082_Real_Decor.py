import time


def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print("Total time take by Func ->", end_time - start_time)

    return wrapper()


def print_logs(func):
    def wrapper():
        print("Starting Log")
        func()
        print("Ending Log")

    return wrapper()


@time_decorator
@print_logs
def test_ui_1():
    print('Add a function, time taken by function1')
    time.sleep(2)


@time_decorator
@print_logs
def test_ui_2():
    print('Add a function, time taken by function2')
    time.sleep(5)
