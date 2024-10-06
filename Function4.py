def student_details(name,usn,age):
    name = input("Enter your name:")
   
    
    usn = input("Enter your USN:")

    age = int(input("Enter your age:"))
    if age <0:
        print("age cannot be zero")
    elif age <18:
        print("age cannot be less than 18")
    elif age > 18:
        print("Your are eligible for this course ")
    else:
        return False

    print(f"Welcome {name}")
    print(f"Your USN is {usn}")
   
    if age >18:
         print(f"Your age is {age}")
    else:
         print("you are not allowed")
    

# student_details(name,usn,age)
student_details("vini","1st21cs236",16)