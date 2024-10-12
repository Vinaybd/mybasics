#Simple my built program 

email ="vinay@gmail.com"

while True:
   email = input("Enter your email address :")
   if "@" in email and "." in email :
     print("Valid email address")
     break
   else :
     print("Invalid email address")
     break
   
while True :
  usn = input("Enter your usn (1ST21CS236) :")

  if "ST" in usn and "21" in usn :
       print("Valid usn ")
       break
  else:
    print("Invalid usn ")
    break
  
Branch = ("Enter your branch :")

Age = int(input("Enter your age :"))

if Age >= 18 and Age <= 25 :
    print("You are eligible for above scheme")

else:
    print("You are not eligible for above scheme")

    # Assignment
    
marks = int(input("Enter your marks :"))
if marks >= 90 :
    print("Grade A")
elif marks >= 80 :
    print("Grade B")
elif marks >= 70 :
    print("Grade C")
else:
    print("Grade D")



