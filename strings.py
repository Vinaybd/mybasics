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