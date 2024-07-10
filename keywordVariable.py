def person(name,**data): 
    # ** indicates we can use multiple parameters or keywords
    print(name)
    print(data)

    for i,j in data.items():
        print(i,j)
person('vijay',age='28',place='mumbai',mobil=987654321)