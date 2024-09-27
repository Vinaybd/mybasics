
items =["vini","viji",'vishwa']
# for i in range(0,len(items)):
print(items[2])
items.pop() #it removes the items
items.append("vishnu") #add item to  the list
items.remove("viji")
items.insert(1,"varun")#insert into a mentioned index positionS
items[0]="vinay"
items.append("chetu")
items.insert(3,"kari")
print(items)

#slicing
#list =[start:end:step]
l=[100,200,300,400,500]
l2=l[1:3]
l=l[3:]
print(l2)
print(l)

#sorting
items=[10,80,45,32,67,84,70]
# print(sorted(manu))
sorted_items=sorted(items) #items is sorted
rev=sorted_items.reverse() #items will be reversed
print(sum(items))
print(items.count(45))
print(sorted_items)