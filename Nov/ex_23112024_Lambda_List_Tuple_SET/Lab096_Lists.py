my_list = [1, 2, 3]

# Indexing
print("Element at the index 0 -", my_list[0])
print("Element at the index 1 -", my_list[1])
print("Element at the index 2 -", my_list[2])

# append() ->Append item at the end of the list
my_list.append(4)
my_list.append(5)
print(my_list)

# extend() ->add another list to the list
my_list.extend([7, 8, 10, 9])
print(my_list)

# insert()-->adding any item at a specific location
my_list.insert(1, "Kiran")
print(my_list)
print(len(my_list))

my_list[2] = "Singh"
print(my_list)

# Remove
my_list.remove("Kiran")
print(my_list)

# copy() -->Copy the list
my_list2 = my_list.copy()
print(my_list2)
my_list2.remove("Singh")
print(my_list2)

# sort
my_list2.sort()
print(my_list2)
