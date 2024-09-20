#python calculator

operator = input("Enter the operation(+,-,*,/)")
num1=float(input("Enter the 1st number:"))
num2=float(input("Enter the 2nd number:"))

if operator =="+":
    result=num1+num2
    print(round(result,3)) #,3 will gives the 3 decimal point after the point
elif operator=="-":
    result=num1-num2
    print(round(result))
elif operator=="*":
    result=num1*num2
    print(round(result))
elif operator=="/":
    result=num1/num2
    print(round(result))
else:
    print(f"{operator} is not an valid input")