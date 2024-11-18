#Task #1: Write a program to take a user age and let him know if he can go the club.  21

#Step 1: Figure out Input & Output
#Input ->Age -Integer
#Output->Can go to Club if age OR Can't go to Club

age = int(input("Please enter your age:\n"))

#Step 2: Rough Logic
#Can go to Club if age >=21 OR Can't go to Club if age <21

#Step 3: Logic
if (age >= 21) and (age <143):
    print("Yes,You can go to Club")
elif age >=143:
    print("Invalid age")
else:
    print("No, You can't go to Club")