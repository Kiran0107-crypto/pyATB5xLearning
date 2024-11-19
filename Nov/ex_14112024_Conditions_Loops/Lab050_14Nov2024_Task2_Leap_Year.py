"""Checking for a Leap Year , 2024 → Yes
Leap day occurs in each year that is a multiple of 4,
except for years evenly divisible by 100 but not by 400."""

# Logic Building
# Step1:
# Input-> year ->Int
# Output -> Str ->Leap year , Not Leap Year

# Step2:
# Rough Logic
# if year % 100 == 0 and year % 400 != 0
# print(f"{year} is not a Leap Year")
# elif year % 4 == 0:
# print(f"{year} is a Leap Year")
# else:
# print(f"{year} is not a Leap Year")

# Approach 1:
year = int(input("Enter year:\n"))
if year % 100 == 0 and year % 400 != 0:
    print(f"{year} is not a Leap Year")
elif year % 4 == 0:
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")

# Approach 2:
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")
