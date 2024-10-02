import random

# print(help(random))

low =1
high=100
options = ("rock","paper","scissors")
choice = ("A","B","C","D")
foods =("Dosa","puri","Idli","vade","Bath")

number = random.randint(1,20)

number = random.randint(low,high)
options = random.choice(options)
choice = random.choice(choice)

food = random.choice(foods)
print(food)
print(options)
print(choice)
print(number)