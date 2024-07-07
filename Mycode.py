x=int(input("enter a number"))
y=int(input("enter another number"))
z=int(input("enter third number"))
if(x>y and x>z):
    print("X is a greater number")
else:
    print("x is lesser number")
    if (y > x and y> z):
        print("y is a greater number")
    else:
        print("y is lesser number")
        if (z > y and z > x):
            print("z is a greater number")
        else:
            print("z is lesser number")