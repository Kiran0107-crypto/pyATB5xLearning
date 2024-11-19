# Grade Calculator
# Write a program that calculates and displays the letter grade for a give numerical score
# (e.g., A,B,C,D, or F) based on the following grading scale:
# A: 90 -100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# Logic Building Formula

# Step1
# Input ->Score or Marks ->int
# Output -> Str ->A / B /C....

score = int(input("Enter your score:\n"))

# if score >= 90 and score <= 100 -->A
if (score >= 90) and (score <= 100):
    print("Your grade is", "A")
# if score >=80 and score <=89 -->B
elif (score >= 80) and (score <= 89):
    print("Your grade is", "B")
# if score >=70 and score <=79 -->C
elif (score >= 70) and (score <= 79):
    print("Your grade is", "C")
# if score >=60 and score <=69 -->D
elif (score >= 60) and (score <= 69):
    print("Your grade is", "D")
elif (score > 100) or (score < 0):
    print("You are Superman!!, Your can't get a grade!!")
# if score >=0 and score <=59 -->F
else:
    print("Your grade is", "E")
