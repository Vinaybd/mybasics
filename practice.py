# # # name="vini"
# # # age=22
# # # is_student=False
# # # weight=68.0

# # # print(type(is_student))
# # # is_student="vini"
# # # print(type(is_student))

# # # s="100"
# # # print((int(s)+age))

# # a=20
# # b=30
# # # print(a+b)
# # # print(a+b-a+b*2**3) #it will follow bodmass technique

# # a,b=b,a
# # print(a)
# # print(b)

# # unit=input("Enter the temperature in Celsius or Fahrenheit (C/F):")
# # temp =float(input("Enter the temperature :"))

# # if unit == 'C':
# #     temp= (temp*12,1)
# #     print(f"Temperature is :{temp} ")

# # elif unit == 'F':
# #     temp= ((temp-32)*5/9,1)
# #     print(f"Temperature is :{temp} ")
# # else:
# #     print(f"Invalid Input {temp}") 

# # boy_name = input("Enter the boy name :")
# # boy_age = int(input("Boy age:"))
# # girl_name = input("Enter the girl name :")
# # girl_age = int(input("girl age:"))

# # ''' wt was the resom '''
# # age_diff =abs( boy_age -girl_age)

# # print(f"{boy_name} Loves the girl {girl_name}.Age diff is {age_diff}")
# # print(boy_name + " Loves " + girl_name)

# # first_name = "vini"
# # last_name = "Dacchu"
# # full_name = first_name + " " + last_name
# # print(full_name)

# message = "  Hello, World!  "
# print(message.strip())  # Output: "Hello, World!"
# print(message.upper())  # Output: "HELLO, WORLD!"
# print(message.replace("World", "Python"))  # Output: "Hello, Python!"

# name = input("Enter your name:")
# name.find("")
# name.isalpha()
# if len(name) > 12:
#     print("username should not exceed 12 character")
# elif  " " in name:
#     print("Username should not contain spaces")
# elif not  name.isalpha() :
#     print("Username must be alphabetics")
# else:
#     print(f"Hello {name}")

#strings

first_name = "vinay"
last_name = "dacchu"
full_name = first_name+ ""+last_name
print(full_name)

message = " warning! "
print(message.strip())
print(message*10)
print(message.replace("warning!","error!"))
print(message.endswith("t,s"))

name = '''"vinay said 'hello' "
        "manu said 'hi'" '''
print(name)
print(len(name)) #length

#accesing string character
name = "Vinay"
print(name[4]) #index=pos-1
print(name[-1])
print(name[-5])
print(name[-1:])
print(name[0:5])
print(name[::2])

#escape sequence

s="vinay is a good boy \n" #\n will give nxt line
v="chethan \n is good"
m="manju \t is fine" #\t will give much space
print(s)
print(v)
print(m)

name=input("enter your name:")
age =input("enter your age:")
print(f"Hello,{name} you are {age} years old")

name =input("enter ypour name:")
print(len(name))
