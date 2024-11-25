#Find the first non-repeating character in a string using sets
#Swiss ->

def first_non_repeating(string):
    for char in string:
        if string.count(char)==1:
            return char
    return None

#Print all non-repeating charaters
def all_non_repeating(string):
    for char in string:
        if string.count(char)==1:
            print(char,end=" ")
    return None

print(first_non_repeating('swiss'))
print(first_non_repeating('pepper'))
print(first_non_repeating('dada'))
print(first_non_repeating('annusinha'))

print("=======================")
print(all_non_repeating('swiss'))
print(all_non_repeating('pepper'))
print(all_non_repeating('dada'))
print(all_non_repeating('annusinha'))