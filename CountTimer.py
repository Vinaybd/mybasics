# default function is used

import time

# def count(start,end): this is nrml funct inside only we can represt start 
#                       but we hve to write after writing first parameter
def count(end,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("Done")

# count(0,10) #this is for first one whc not made start =0 in paramter
# count(10)
count(30,15)