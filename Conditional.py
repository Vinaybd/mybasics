# Conditonal expression = A  one line shortcut for if -else statement (ternary operator)
#                        print or assign one of two values based on a condition
#                       X if condition else Y

num = 5
a = 6
b = 7
age = 16
temperature = 30
user="vinay"

print("Positive" if num>0 else "Negative" )
result = "Even" if num % 2  == 0 else "Odd"
max_num = a if a > b else b
min_num = a if a <b else b
status = "Adult" if age >=18 else "Child"
weather = "Hot" if temperature >= 30 else "Cold"
aunthentication = "True" if user == "vini" else "False"
print(min_num,max_num)
print(status)
print(weather)
print(aunthentication)