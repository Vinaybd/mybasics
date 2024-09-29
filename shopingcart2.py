items =[]
prices =[]
total =0
while True:
    item = input("Enter the item name (q to quit) :")
    if item.lower()=="q":
        break
    else:
        price = float(input("Enter the price of the item:"))
        items.append(item)
        prices.append(price)
print("Your cart")

for item in items:
    print(item)

for price in prices:
    print(price)
    total = price + total
print(f"Total items price: {total}")
