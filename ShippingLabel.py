def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg,end=" ")
    print()

    # for value in kwargs.values():
    #     print(value,end=" ")
    
    # we can also use if and else statements
    #whether to  print strea or other like that
    
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} ,{kwargs.get("zip")}")

shipping_label("Dr.","Vinay","Dacchu","IT",
              street ="Blr",
               apt ="100",
                city ="Bangalore",
                state ="Karnataka",
                zip_code ="560078",
                country ="India")