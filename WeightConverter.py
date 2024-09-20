
weight = float(input("enter your weight:"))
unit = input("Kilograms or Ponds? (K or L):")

if unit == "K":
    weight=weight * 2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight /2.205
    unit = "Kgs."
else:
    print(f"{unit} was not valid")

print(f"Your weight is : {round(weight,1)} {unit}")