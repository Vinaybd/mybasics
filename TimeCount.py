import time
5
my_time =int( input("enter the time in seconds"))

# for x in (range(0,my_time):#used for direct range 
for x in range(my_time,0,-1):#used for reverse
    seconds = x % 60
    minutes = int(x/60)%60
    hours = (x/3600)
    print(f"{hours:20}:{minutes:02}:{seconds:02}")
    # print(x)
    time.sleep(1)

print("Times up")