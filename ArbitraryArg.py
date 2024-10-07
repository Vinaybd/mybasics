# *args = allow you to pass multiple non-key arguments
# **kwargs = allow you to pass multiple keyword arguments
#             *unpacking operator

def add(*args):
    total =0
    for arg in args:
        total += arg
    return total

print(add(1,2,3))


def display_name(*args):
    for arg in args:
        print(arg,end=" ")

display_name("Vini","Vijay","Vishwa")


#** kwargs

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_address(street ="123 st  ft",
              apt="100",
              city="Bangalore",
              state="karnataka",
              zip=560097)