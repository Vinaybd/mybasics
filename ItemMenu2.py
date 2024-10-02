
items ={
     "Food":20.0,
     "Tea Powder":20.0,
     "cofee": 30.0,
     "Dal":65.0,
     "Oil":80.0,
     "Sugar":25.0
}

Track =[]
total =0

for key,value in items.items():
     print(f"{key}:{value}")

while True:
     item = input("Select the item u want (q to quit):")
     if item.lower() =="q":
          break
     elif items.get(item) is not None:
          Track.append(item)

for item in Track:
     total = total + items.get(item)
     print("item",end=" ")

print()
print(f"Your total items is of cost ${total}")