student_infor1 = {
    "name": "Kiran",
    "age": 67,
    "address": {
        "home_address": "ND",
        "office_address": "KA"
    }
}

student_infor2 = {
    "name": "Jay",
    "age": 67,
    "address": {
        "home_address": "ND",
        "office_address": "KA"
    }
}

student_infor3 = {
    "name": "Maya",
    "age": 120,
    "address": {
        "home_address": "LTP",
        "office_address": "UP"
    }
}

student_list = [student_infor1, student_infor2, student_infor3]
print(student_list)
print(student_list[0])
print(student_list[1])
print(student_list[2])

print(student_list[0]["name"])
print(student_list[0]["age"])
print(student_list[0]["address"])
print(student_list[0]["address"]["office_address"])

print(student_list[2]["address"]["office_address"])
