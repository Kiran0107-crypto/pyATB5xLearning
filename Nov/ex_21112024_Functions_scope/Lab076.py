public_toilet = "PB"


def home():
    private_toilet = "PT"
    print(private_toilet)
    print(public_toilet)


def stranger():
    print(public_toilet)
    # print(private_toilet) ->private_toilet can't be used inside another function as
    # it local to home() function


print(public_toilet)
# print(private_toilet) ->private_toilet can't be used inside another function as
# it local to home() function
