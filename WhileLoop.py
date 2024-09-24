# while loop = execute some code While some condition remains true

name = input("Enter your name:")

#this is if conditon we can also use tis but it doest hold good as while takes
# if name == "":
#     print("You did not enter your name")
# else:
#     print(f"hello {name}")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name:")

print(f"Hello {name}")

age=int(input("enter your age:"))
while age <0:
    print("Age cannot be negative:")
    age = int(input("enter your age:"))
print(f" You are {age} years old")

height=int(input("enter your hegight:"))

while height<0:
    print("Hegight must be some value:")
    height = int(input("Enter your height:"))
print(f"Your height is {height} cm")


food = input("Enter a food you like(q to quit):")

while food != 'q':
    print("enter the food you like to have:")
    food = input("Enter another food which you like to have:")
print("Thank you bye ")

num = int(input("enter a number between 1 -10:"))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("enter a number between 1 -10:"))
print(f"Your number is{num}")