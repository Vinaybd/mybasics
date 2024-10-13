def marrage(boy,girl):
    print(f"Boy is {boy}")
    print(f"Girl is {girl}")
    print(f"{boy} married {girl}")
marrage("Vinay","Muddu")


def func(num):
    return int(str(num)*5)

a=100
b=func(2)
c= a+ func(2)

print(c)

#local and global variable

def func():
    x="vinay"  #local variable
    print("Hello World")
    print(y)

y = "vijay" #global variable

print(y)