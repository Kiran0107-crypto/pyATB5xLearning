set1={1,2,3}
set2={4,5,6}
my_set=set1.union(set2)
print(my_set)

set3={1,2,3,4,5}
set4={4,5,6,7,8}
my_set2=set3.intersection(set4)
print(my_set2)

my_set3=set3.difference(set4)
print(my_set3)
my_set4=set4.difference(set3)
print(my_set4)