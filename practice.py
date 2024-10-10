# # # # # name="vini"
# # # # # age=22
# # # # # is_student=False
# # # # # weight=68.0

# # # # # print(type(is_student))
# # # # # is_student="vini"
# # # # # print(type(is_student))

# # # # # s="100"
# # # # # print((int(s)+age))

# # # # a=20
# # # # b=30
# # # # # print(a+b)
# # # # # print(a+b-a+b*2**3) #it will follow bodmass technique

# # # # a,b=b,a
# # # # print(a)
# # # # print(b)

# # # # unit=input("Enter the temperature in Celsius or Fahrenheit (C/F):")
# # # # temp =float(input("Enter the temperature :"))

# # # # if unit == 'C':
# # # #     temp= (temp*12,1)
# # # #     print(f"Temperature is :{temp} ")

# # # # elif unit == 'F':
# # # #     temp= ((temp-32)*5/9,1)
# # # #     print(f"Temperature is :{temp} ")
# # # # else:
# # # #     print(f"Invalid Input {temp}") 

# # # # boy_name = input("Enter the boy name :")
# # # # boy_age = int(input("Boy age:"))
# # # # girl_name = input("Enter the girl name :")
# # # # girl_age = int(input("girl age:"))

# # # # ''' wt was the resom '''
# # # # age_diff =abs( boy_age -girl_age)

# # # # print(f"{boy_name} Loves the girl {girl_name}.Age diff is {age_diff}")
# # # # print(boy_name + " Loves " + girl_name)

# # # # first_name = "vini"
# # # # last_name = "Dacchu"
# # # # full_name = first_name + " " + last_name
# # # # print(full_name)

# # # message = "  Hello, World!  "
# # # print(message.strip())  # Output: "Hello, World!"
# # # print(message.upper())  # Output: "HELLO, WORLD!"
# # # print(message.replace("World", "Python"))  # Output: "Hello, Python!"

# # # name = input("Enter your name:")
# # # name.find("")
# # # name.isalpha()
# # # if len(name) > 12:
# # #     print("username should not exceed 12 character")
# # # elif  " " in name:
# # #     print("Username should not contain spaces")
# # # elif not  name.isalpha() :
# # #     print("Username must be alphabetics")
# # # else:
# # #     print(f"Hello {name}")

# # #strings

# # first_name = "vinay"
# # last_name = "dacchu"
# # full_name = first_name+ ""+last_name
# # print(full_name)

# # message = " warning! "
# # print(message.strip())
# # print(message*10)
# # print(message.replace("warning!","error!"))
# # print(message.endswith("t,s"))

# # name = '''"vinay said 'hello' "
# #         "manu said 'hi'" '''
# # print(name)
# # print(len(name)) #length

# # #accesing string character
# # name = "Vinay"
# # print(name[4]) #index=pos-1
# # print(name[-1])
# # print(name[-5])
# # print(name[-1:])
# # print(name[0:5])
# # print(name[::2])

# # #escape sequence

# # s="vinay is a good boy \n" #\n will give nxt line
# # v="chethan \n is good"
# # m="manju \t is fine" #\t will give much space
# # print(s)
# # print(v)
# # print(m)

# # name=input("enter your name:")
# # age =input("enter your age:")
# # print(f"Hello,{name} you are {age} years old")

# # name =input("enter ypour name:")
# # print(len(name))

# # print(not(False))
# # print(not(1>2))

# items =["vini","viji",'vishwa']
# # for i in range(0,len(items)):
# print(items[2])
# items.pop()
# items.append("vishnu")
# items.remove("viji")
# items.insert(1,"varun")
# items[0]="vinay"
# items.append("chetu")
# items.insert(3,"kari")
# print(items)

# #slicing
# #list =[start:end:step]
# l=[100,200,300,400,500]
# l2=l[1:3]
# l=l[3:]
# print(l2)
# print(l)

# #sorting
# items=[10,80,45,32,67,84,70]
# # print(sorted(manu))
# sorted_items=sorted(items) #items is sorted
# rev=sorted_items.reverse() #items will be reversed
# print(sum(items))
# print(items.count(45))
# print(sorted_items)

# #matrix 
# m=[[1,2],[3,4],[5,6]]
# print(m)
# print(m[0])
# print(type(m))

#tuples and sets

# gender =("male",)
# # gender[0] = "un"
# # print(gender[1])

# sex = "nija"
# new = gender +(sex,)
# print(gender)
# print(new)

# a = ('2',)
# b = 'z'
# new = a + (b,)
# print(new)

# # sets
# # sets are unique unordered and unindex then it will not allow duplicate values
# #                Sets are useful for performing operation  like union,insertion,and difference
# s1={20,13,45,2}
# # s2 = set(1,2,3)
# s2 = {1,2,3}
# s3 =set() # empty set
# print(s1)
# print(s1|s2) #union
# print(s1&s2) #intersection
# print(s1-s2) #difference

# s={1,2,3,4,5,}
# # s.pop() #this func pop the first element
# s.remove(2)#it will directly remove the second element
# s.discard(3)#this will check if element their in set then remove that
# s.add(6)
# print(s)


# menu ={
#     "Juice":20.0,
#     "Pizza":80.0,
#     "Cocktail":70.0,
#     "Tea":80.0,
#     "Burger":100.0,
#     "Frenchfries":50.0

# }

# cart =[]
# total =0

# for key,value in menu.items():
#     print(f"{key}:{value}")
 

# while True:
#         food = input("select your food(q to quit):")
#         if food.lower() =="q":
#               break
#         elif menu.get(food) is not None:
#             cart.append(food)
    
# print("----Your Order-----")
# for food in cart:
#      total = total +menu.get(food)
#      print("food",end=" ")

# print()
# print(f"{food} is available on your table ur bill is {total}")

#for loop
# A for loop allows you to repeat a block of code a fixed number of times, 
# --or once for each element in a sequence.

# v1=range(1,18,2)
# print(v1)

# i=1
# for i in range(1,10):
#     print(i,end=" ")
#     i+=1


# names = ("vini","viji","vishwa")
# for i in names:
#     print(i,end=" ")
# i=1
# for i in range(1,18,3):
#     print(i,end=" ")

# name ="vinay"

# for i in name:
#     print(i*2)

# name ="vinay"

# for index, i in enumerate(name): # enumerate func gives the index of each letter
#     # print(i*2)
#     print(i*(index+1))

# l =[12,1234,14,122]
# for num in l:
#     print(num)
#     if num == 14:
#         break
# else:
#     print("All Printed")

# d={"name":"vinay","age":20,"income":1}
# # print(d.items())

# for key,value in d.items():
#     print(f"{key}:{value}")

#nested loops 
#multiplication tables

# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i}*{j}={i*j}",end="\t")
#     print()

# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i}*{j}={i*j}")
#     print("------------------")
#     # print(f"2*{i}={2*i}")

# laddus = 5
# friends = ["Rahul", "Sneha", "Aman", "Priya"]

# for friend in friends:
#     if laddus > 0:
#         print(f"{friend} gets a laddu!")
#         laddus -= 1
#     else:
#         print("No laddus left!")

# i=1
# for i in range(1,30,3):
#     print(i)

# for i in range(1,11):
#     print(f"3*{i}={3*i}")

#finding total 

# l = [1,23,43,543,678]
# total =0

# for  i in l:
#     print(total)
#     total = total + i

# print(f"Total is {total}")


# l=[1,24,56,78,98,99]
# D=[]

# for num in l:
#     if num % 2 ==0:

#       D.append(num*2)
#     else:
#       print(D)
#     print(D)


# #using dictionary
# student_marks ={"Anand":85,"Geetha":90,"kumar":78}
# student_marks ={"Anand":85,"Geetha":90,"kumar":78}
# marks =[25,30,45]

# for name , marks in student_marks.items():
#     print(f"{name} scored {marks}")

# #using lists

# student =["Anand","Geetha","kumar"]

# marks =[85,90,78]

# student_marks={} #we r displaying the index position with element using dictionary

# #one method
# for index,student in enumerate(student):
#     student_marks[student] = marks[index]

# #another method

# for i in range(len(student)):
#     student_marks[student[i]] = marks[i]

# print(student_marks)

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