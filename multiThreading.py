#multiple tasks in one time then cpu will doo it properly
#every applications have different threads so cpu will automatically handles it
from threading import *
from time import sleep #its hold the function for few seconds


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1) #delay for 1 second


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1) #delay for 1 second
 
t1=Hello()
t2=Hi()

t1.start()
sleep(0.2)  # delay for 0.2 second before starting t2 thread
t2.start()

t1.join() #wait until t1 finishes

t2.join() #wait until t2 finishes
print("bye")
          