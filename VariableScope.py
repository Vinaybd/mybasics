# Variable scope = where  a variable is visible and accessible
# scope resolution = (LEGB) local -> Enclosed -> Global -> Built-in

def fun1():
    x=1
    print(x)
def fun2():
    x=3
    print(x)

fun1()


def fun1():
    
    print(x)
def fun2():
    
    print(x)

x=3

fun1()
fun2()


from math import e

def func3():
    print(e)

e=3

func3()


def func4():
    print(e)

e = 8

func4()