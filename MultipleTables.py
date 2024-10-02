
#nested loops 
#multiplication tables

for i in range(1,11):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}",end="\t")
    print()

for i in range(1,11):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")
    print("------------------")
    # print(f"2*{i}={2*i}")

#program 
laddus = 5
friends = ["Rahul", "Sneha", "Aman", "Priya"]

for friend in friends:
    if laddus > 0:
        print(f"{friend} gets a laddu!")
        laddus -= 1
    else:
        print("No laddus left!")

i=1
for i in range(1,30,3):
    print(i)


#asignment for multiplication
for i in range(1,11):
    print(f"3*{i}={3*i}")