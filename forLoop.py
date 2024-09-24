# for loops = executes a block of code a fixed number of times.
#     we can iterate over a range,string,sequence,etc.



for x in reversed(range(12,25,2)): #(start,end) which is range
    print(x)                     #(start,end,step) if we use step value
print("Happy birth day")

for x in range(11,25):
    if x ==21:
        continue # continue will skip the mentioned number
        # break # it breaks and comes out of the loop
    else:
        print(x)

for vini in range(10,200,5):
    if vini == 50:
        continue
    else:
        print(vini)
        if vini ==120:
            break
