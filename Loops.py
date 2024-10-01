i =0

while i < 10:
    x=0
    while x<i:
        print("Vinay",end="-")
        x += 1
    print("")
    i += 1

#assignment
pin ="1234"  
input_pin =True
trails =0
while trails<=3:
    input_pin =input(f"Trail-{trails}PIN >> :")
    trails += 1
    if input_pin == pin:
        print("CORRECT")
        break
    else:
        print("INCORRECT")