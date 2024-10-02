# for loop
# A for loop allows you to repeat a block of code a fixed number of times, 
# --or once for each element in a sequence.

v1=range(1,18,2)
print(v1)

i=1
for i in range(1,10):
    print(i,end=" ")
    i+=1


names = ("vini","viji","vishwa")
for i in names:
    print(i,end=" ")
i=1
for i in range(1,18,3):
    print(i,end=" ")

name ="vinay"

for i in name:
    print(i*2)

name ="vinay"

for index, i in enumerate(name): # enumerate func gives the index of each letter
    print(i*2)
    print(i*(index+1))

l =[12,1234,14,122]
for num in l:
    print(num)
    if num == 14:
        break
else:
    print("All Printed")

d={"name":"vinay","age":20,"income":1}
print(d.items())

for key,value in d.items():
    print(f"{key}:{value}")

