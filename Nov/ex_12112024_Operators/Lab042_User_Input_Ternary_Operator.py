# Program; if age > 18--->Allowed to Vote
# else -> not allowed to Vote
user_age = int(input("Enter your age"))
if user_age >= 18:
    print("Yes,You are allowed to go to Goa & Vote")
else:
    print("No, You are not allowed to go to Goa & Vote")

print("######################")
# Above using Ternary ---Not recommended and not easy to understand
print("Yes,You are allowed to go to Goa & Vote" if int(
    input("Enter your age")) >= 18 else "No, You are not allowed to go to Goa & Vote")
