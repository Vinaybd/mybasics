#Students registration

email ="vinay@gmail.com"
usn = "1ST21CS236"
branch = "CS"
age = 18
marks = 45

while True:
   email = input("Enter your email address :")
   if "@" in email and "." in email :
   
        print("Valid email address")
        break
   else :
        print("Invalid email address")
  
   
while True : 
  usn = input("Enter your usn (1ST21CS236) :")

#   if "ST" in usn and "21" in usn :
#        print("Valid usn ")
#        break
  if usn == True:
    print("Valid usn")
  else:
    print("Invalid usn please try again ")
    usn = input("Enter your usn (1ST21CS236) :")
    break
  
Branch = input("Enter your branch :")

Age = int(input("Enter your age :"))

if Age >= 18 and Age <= 25 :
    print("You are eligible for above scheme")

else:
    print("You are not eligible for above scheme")

    # Assignment
    
marks = int(input("Enter your marks :"))
if marks >= 90 and marks<=100 :
    print("Grade A")
elif marks >= 80 and marks<90 :
    print("Grade B")
elif marks >= 70 and marks<80:
    print("Grade C")
elif marks >100 :
    print("Marks should be between 0 and 100")
    marks = int(input("Enter your marks :"))
else:
    print("Grade D")



