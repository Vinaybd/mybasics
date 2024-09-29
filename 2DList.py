
fruits = ["apple","orange","banana","cocoa"]
vegetables = ["tomato","potato","chilli","onion"]
meats = ["chiken","fish","turkey"]

groceries = [fruits,vegetables,meats]
 # we can use all the lists in one lists
print(groceries[1]) #print 1st list
print(groceries[0][1]) #print 1st element in the 0th list
print(groceries[1][3]) #print 3rd element in 1st list

for collection in groceries:
    # print(collection)
    for food in collection:
        print(food)
    print()