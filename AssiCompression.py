#Create a list of Kannada foods. Use list comprehension to
# create a new list where each food name is in uppercase.

food=["idli","vade","sambar","pulav","puri"]

dl =[item.upper() for item in food]
print(dl)

#Create a dictionary of 5 items with their prices. Write a program
#  that calculates the total price of all items using a for loop.

items ={
    "pen":5,
    "pencil":10,
    "book":30,
    "notes":50,
    "eraser":2
}

total_price =0

for item in items:
    total_price += items[item]
print(total_price)

#Create a list of numbers from 1 to 10.
# Use list comprehension to generate a list of their squares.

list =[x for x in range(1,11)]

squares=[x**2 for x in list]

print(squares)


#Create a list of 3 dictionaries, 
# where each dictionary contains the name, age, and marks of
# a student. Loop through the list and print each student's information.

student1={
    "name":"John","age":20,"marks":80}
student2={
    "name":"Jane","age":22,"marks":95}
student3={
    "name":"David","age":21,"marks":75
}
# students={}
# students.update(student1)
# students.update(student2)
# students.update(student3)

students ={**student1,**student2,**student3}


student_list={key:value for key,value in students.items()}
print(student_list)


#another method
# Creating a list of dictionaries
students = [
    {'name': 'Alice', 'age': 20, 'marks': 85},
    {'name': 'Bob', 'age': 22, 'marks': 90},
    {'name': 'Charlie', 'age': 21, 'marks': 88}
]

# Looping through the list to print each student's information
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")

#Create a dictionary where the keys are Kannada cities, and the values are their populations.
#  Use dictionary comprehension to filter out cities with populations below 10 lakhs.

kannada_cities = {
    "Bengaluru": 1000000,
    "Mysuru": 1100000,
    "Hubballi": 9000000,
    "Mangaluru": 500000
}
large_cities = {city: population for city, population in kannada_cities.items() if population > 1000000}
print(large_cities)


#Nested List Challenge: Write a Python program that takes a list of lists (a 2D list) as input and:

     #Prints the entire matrix row by row.
    #Prints the sum of each row in the matrix.



# Sample 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print the entire matrix row by row
print("Matrix:")
for row in matrix:
    print(row)

# Print the sum of each row in the matrix
print("\nSum of each row:")
for index, row in enumerate(matrix):
    row_sum = sum(row)
    print(f"Sum of row {index + 1}: {row_sum}")
