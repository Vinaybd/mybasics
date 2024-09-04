from abc import ABC,abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("Laptop is processing...")

class Whiteboard():
    def write(self):
        print("Whiteboard is writing...")
        
class Programmer:
    def work(self,com):
        print("I am writing...")
        com.process()
com1=Laptop()
com2=Whiteboard()


prog1=Programmer()
prog1.work(com1)
