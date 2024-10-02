menu ={
    "Juice":20.0,
    "Pizza":80.0,
    "Cocktail":70.0,
    "Tea":80.0,
    "Burger":100.0,
    "Frenchfries":50.0

}

cart =[]
total =0

for key,value in menu.items():
    print(f"{key}:{value}")
 

while True:
        food = input("select your food(q to quit):")
        if food.lower() =="q":
              break
        elif menu.get(food) is not None:
            cart.append(food)
    
print("----Your Order-----")
for food in cart:
     total = total +menu.get(food)
     print("food",end=" ")

print()
print(f"{food} is available on your table ur bill is {total}")