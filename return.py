#return = statement used to end a function
#      and send a result back to the caller

#simple funtion
def add(x,y):
    z=x+y
    return z

def sub(x,y):
    z=x-y
    return z

def mul(x,y):
    z=x*y
    return z

def div(x,y):
    z=x/y
    return z

print(add(3,4))
print(sub(3,4))
print(mul(3,4))
print(div(3,4))


def create_name(first,last):

    # we are capitalized separately or we can directly do in return func
    first = first.capitalize()
    last = last.capitalize()
    #directly capitaized here
    return first.capitalize() + " " + last.capitalize()

full_name = create_name("vini","dacchu")
print(full_name)