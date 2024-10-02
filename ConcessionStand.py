#Concession stand program

menu ={
    "Coke": 1.5,
    "Pepsi": 1.75,
    "Sprite": 1.75,
    "Water": 1.25,
    "Soda": 1.0,
    "Pizza":3.00,
    "Lemosoda":2.0,
    "French Fries": 1.0,
    "Burger": 2.50
}

cart =[] #to keep track of the menu
total =0

print("--------MENU--------")
for key,value in menu.items():
    print(f"{key:10}:${value:.2f}")
print("--------------------------------")

while True:
    food=input("Select an item (q to quit):")
    if food.lower() =="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("-----Your order ------")
for food in cart:
    total = total + menu.get(food)
    print(food,end=" ")

print()

print(f"Your total is : ${total:.2f}")
