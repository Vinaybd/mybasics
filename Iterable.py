# Iterable = An object/collector that can return its elements one at a time,
#            allowing it to be iterate over in loop

numbers = [1,2,3,4,5]

for item in reversed(numbers):
    print(item)


fruits = ("apple","orange","banana","coconut")

for fruit in reversed(fruits):
    print(fruit)

#strings
name = "Bro Code"

for character in name:
    print(character)

#dictionary

my_dictionary = {"A":1,"B":2,"C":3}

for key,value in my_dictionary.items():
    print(f"{key}:{value}")