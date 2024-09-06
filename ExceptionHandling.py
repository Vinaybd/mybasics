
a=5
b=2

    
try:
    print("resource open")
    print(a/b)
    k=int(input("Enter a number"))
    print(k)
  
   
except ZeroDivisionError as e:
    print("Hey,You cannot enter a zero for division",e)

except ValueError as e:
    print("Invalid input")

except Exception as e:
    print("Something went Wrong...")

finally:   
    print("resource close")
 