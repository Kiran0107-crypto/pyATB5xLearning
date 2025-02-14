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

student_list = [student_infor1, student_infor2]
print(student_list)
print(student_list[0])
print(student_list[1])

print(student_list[0]["name"])
print(student_list[0]["age"])
print(student_list[0]["address"])
print(student_list[0]["address"]["office_address"])
