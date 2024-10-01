
x = 12

if x==10:
    print("you are in the right way:")
elif x==12:
    print("You are just near")
else:
    print("you are in the wrong way:")

signal =input("Enter the color :")

if signal == "red":
    print("Stop")
elif signal =="yellow":
    print("Ready")
elif signal == "Green":
    print("Go")
else:
    print("Unknown signal")

attendence=int(input("Enter your attendence percentage :"))
is_teacher_friend = False

if attendence >=75 :
    print("test")
if attendence <=75 and is_teacher_friend :
    print("test")
if attendence <=75 and is_teacher_friend == False:
    print("No test")

# Assignment

gender =input("Enter your gender:")
age =int(input("Enter your age:"))

if gender == "female":
    print("Tiket is free")
else:
    if age<5:
        print("Tiket is free")
    elif age <=12:
        print("Half tiket")
    elif age>=60:
        print("Seniro citizen half ticket")
    else:
        print("You have to pay full fare")

# Assignment
Age = int(input("enter your age:"))
is_pass = True
if Age<5:
    print("Free bus ticket ")
elif Age>=60 :
    print("Senior citizen bus ticket")
else:
    print("You have to pay full fare")

#Assignment

def meal_time(hour):
    if 8 <= hour < 9:
        return "It's time for breakfast."
    elif 13 <= hour < 14:
        return "It's time for lunch."
    elif 20 <= hour < 21:
        return "It's time for dinner."
    else:
        return "It's not meal time."

try:
    hour = int(input("Enter the hour (0-23) in 24-hour format: "))
    if 0 <= hour <= 23:
        print(meal_time(hour))
    else:
        print("Please enter a valid hour between 0 and 23.")
except ValueError:
    print("Invalid input! Please enter a numeric value.")
