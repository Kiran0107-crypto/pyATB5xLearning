def add_before_ui_after_ui(func):
    def wrapper():
        print("Before running the UI TC")
        print("Start the Browser")
        func()
        print("Editing the running UI TC")
        print('Quit the Browser')

    return wrapper()


@add_before_ui_after_ui
def test_ui():
    print(">>I will test the UI>>")
