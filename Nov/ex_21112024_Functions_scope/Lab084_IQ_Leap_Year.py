def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


year = int(input("Enter Year:\n"))

if check_leap_year(year):
    print(f"Yes, {year} is Leap Year")
else:
    print(f"No, {year} is not Leap Year")
