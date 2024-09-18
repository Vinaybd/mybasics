#input() = this will allow user  to enter the data

name = input("Enter your name:")
age=int(input("How old are u"))

# age=int(age) we can use int in above line itself to avoid more number of code
age = age + 1 # age += 1 if we use age += age+1 it will double the value

print(f"Hello {name} !")
print("HAPPY BDAY")
print(f"You are {age} years old")