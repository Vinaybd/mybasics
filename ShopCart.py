
item = input("What item would you like to buy?:")
price = float(input("What is the price?:"))
qunatity = int(input("How many would you like to buy?:"))

total = price*qunatity

print(f"You have bought {qunatity} x {item} /s")
print(f"your Total is: ${total}")
feedback=int(input("quality"))
if feedback==1:
    print("Thanks for your feedback")
else:
    print("We will make it changes plss visit again")

item_quality=input(True)

if item_quality:
    print("The item is good")
else:
    print("The item is not good")