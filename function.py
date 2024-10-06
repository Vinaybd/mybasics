#function = A block of reusable code
#            place() after the function name to invoke it

def happy_birthday(name,age): #(in this we can pass parameters tat must match with arguments whc was given below)
    print(f"Happy birthday to {name} ")
    print(f"you are {age} years old")
    print("Happy birthday!")

def gift_by(gift_name):
    print("I would like to give you a gift")
    print("I will choose a gift for you")
    print(f"guess the gift {gift_name}")

happy_birthday("Vinay",20) #invoking the function
happy_birthday("Chetu",18) 
happy_birthday("Manju",20) #The arguments whc are passing inside () must match with parametrs

gift_by("Chocolate") #invoking the function