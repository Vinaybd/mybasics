# dictionary contains key value pairs

birthday ={
    "vini" :"11-11-2003",
    "viji" :"10-10-2002",
    "vishwa" :"09-09-2001"
}

meanings ={
    "criket":"group game",
    "bat" : "To hit",
    "ball" : "To throw",
    "wiket" : "To protect"
}

#Accesing the dictionary
print(meanings.get("criket"))
print(birthday.get("vinay","Not found"))
print(birthday.get("vini","not found"))

#Adding to the dictionary
birthday["sudeep"] = "07-06-2002"
print(birthday)
meanings["Stumps"]= "End of the day"
print(meanings)
print(meanings.get("Stumps","Not found"))
print(meanings.get("bat",))

#updating the meanings
birthday ["vijay"] = "12-07-2003"
print(birthday)

#Removing elements from the dictionary
birthday.pop("vini")
print(birthday)

# del birthday["chandan"]
# print(birthday)

print(birthday.keys()) # it will just gives the keys value
print(birthday.values()) #it gives the only value
print(meanings.keys()) # it will just give the keys value
print(meanings.values())

print(birthday.items()) # it will just give the items value

# loist of items using dictionary
item1 ={
    "name" :"Milk",
    "weight" :"1 ltr",
    "price" : "50"
}

item2 =  {
    "name" :"Bread",
    "weight" :"200 grams",
    "price" : "10"
}

item3 ={
    "name" :"Juice",
    "weight" :"1.5 ltr",
    "price" : "45"
}

items =[item1,item2,item3]

print(items)
print(f"total price {item1["price"]+item2["price"]+item3["price"]}")
print(f"Total weight {item1["weight"]+item2["weight"]+item3["weight"]}")
print(f"Total items {item1, item2, item3}")