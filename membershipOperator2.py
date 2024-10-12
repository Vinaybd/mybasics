students = {"Vinay","vijay","Manju"}

student = input("Enter the name of a student:")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} is not a student")


#dictionaries

grades = {"Vini":"A","Viji":"B","Camb":"C","Varun":"D"}

student = input("Enter the name of the student:")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} is not in the grades list")