# List - Collections of Items
# Butter, bread, banana, panner
# Marks: 90, 91, 94,98,87

# Duplicates are allowed
# Multiple different data types are allowed
# Stored with the index-0 to n-1

my_list = [1, 2, 3]  # Same type of data-int
my_list2 = [1, True, "Kiran", 12.34]

print(my_list)
print(my_list2)
print(len(my_list))

print(my_list[0])
print(my_list[1])
print(my_list[2])
# print(my_list[3]) ---> IndexError: list index out of range

print("=======================")
# Iterating items in list
for item in my_list2:
    print(item)
