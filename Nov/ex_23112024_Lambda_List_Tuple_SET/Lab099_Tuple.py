# Tuple
# Collection of Items
# Immutable ->Elements can't be updated
my_tuple = (1, 4, 9, 16, 25)
# my_tuple[3]=64 -->TypeError: 'tuple' object does not support item assignment

shopping_list = ["Bread", "Butter", "Paneer"]
print(shopping_list)
shopping_list[2] = "Milk"
print(shopping_list)

# Real example of tuples
my_tuple1 = ("tta.com", "sdet.live")
print(my_tuple1)
my_api_list = list(my_tuple1)
print(my_api_list)
# my_tuple1[0]='abc.com' --->TypeError: 'tuple' object does not support item assignment
my_api_list[0] = "abc.com"
print(my_api_list)

# Real Case, where we use tuples
API_URLs = ("https://sdet.live/python5x", "https://awesomeqa.com")
print(API_URLs[0])
print(API_URLs[1])
