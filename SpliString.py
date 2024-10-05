#In Python, the split() method allows you to break a string into a list of words or elements 
# based on a specified separator (like space, comma, etc.). This is very useful
#  when you have data in string format and want to convert it into a list.



# name=input("Enter your names(1st name-2nd name):")

# names = name.split("-")

# print(names)

print("List input practice")

# x =input("Enter list on integers:")

#This for loop is used bcs split fucn will gives o/p in string form so we 
#-want that in integer
# for i  in x:
#     i=int(i)
# print(x.split())

# l=[int(num) for num in x]
l=[int(num) for num in input("Enter list on integers:").split()]

print(l)