import random

vini =("yaru","enu","gottilla")

manu = None
vip = random.choice(vini)

while manu not in vini:
    manu = input("Enter your choice (yaru, enu, gottilla): ")

print(f"manu: {manu}")
print(f"vip: {vip}")