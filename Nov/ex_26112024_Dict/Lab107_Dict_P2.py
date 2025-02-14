student_infor = {
    "name": "Pramod",
    "age": 67,
    "address": "KA"
}

print(student_infor["name"])
print(student_infor["age"])
print(student_infor["address"])
student_infor["age"] = 100
print(student_infor["age"])
print(student_infor)

# Another way to create dictionary

student_infor2 = dict(name="Kiran", age=67, address="KA")
print(student_infor2)

student_infor1 = {
    "name": "Kiran",
    "age": 67,
    "address": {
        "home_address": "ND",
        "office_address": "KA"
    }
}

print(student_infor1)
