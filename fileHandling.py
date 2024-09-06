f = open('MyData.txt','r')

# print(f.read())  # read function will featch the data from the f
                 #f is the function which contains data
print(f.readline(5),end="") 
print(f.readline())
print(f.readline())
print(f.readline())

f1=open('abc','w')

for data in f:
    f1.write(data)
          
#we can also do this for image
#we have to use rb instead of r then wb instead of w at the end for condition for printing