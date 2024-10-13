# list comression = A concise way to create lists in python
#                compact and easier to read than traditional loops
#                 [expression for value in iterable if condition]
double =[]
for x in range(1,11):
    double.append(x*2)

print(double)

doubles = [x*2 for x in range(1,11)]
triples = [y*3 for y in range(1,11)]
squares = [z*z for z in range(1,11)]

print(doubles)
print(squares)
print(triples)

fruits = ["apple","orange","bananaa","coconut"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

numbers = [1,-2,3,-4,5,-6]
positive_nums = [num for num in numbers if num>=0]
negative_nums = [num for num in numbers if num<0]
even_nums = [num for num in numbers if num%2==0]
odd_nums = [num for num in numbers if num%2==1]

print(positive_nums)
print(odd_nums)


grades = [85,42,79,90,56,61,30]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)