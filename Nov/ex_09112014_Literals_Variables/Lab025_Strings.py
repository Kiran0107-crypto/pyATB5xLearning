name= "This is a Big Line"
print(type(name))
#name= name+1  -->TypeError: can only concatenate str (not "int") to str
print(name)
name1 = name + str(1)
print(name1)

first_name="Kiran"
middle_name="Bhan"
last_name="Singh"
full_name= first_name + " " + middle_name + " " + last_name
print(full_name)
print(type(full_name))

