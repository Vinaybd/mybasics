# collection = single "variable" used to store multiple values
# list =[] ordered and changable.Duplicate ok
# set = {} unordered and immutable,but Add/Remove Ok.No duplicates
# Tuple = () ordered and unchangeble.Duplicate ok.FASTER

fruits = ["apple", "orange", "banana","coconut"]
print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("apple" in fruits)

fruits[1]="Sapota" #we can change the element in the list with their index value

fruits.append("mango")
print(fruits)
fruits.sort()
for fruit in fruits:

    fruits.remove("apple")
fruits.insert(5,"pineapple")

fruits.reverse()
fruits.clear()
print(fruits.index("apple"))
fruits.pop() # remove the elements

print(fruits.count("coconut"))


print(fruits)