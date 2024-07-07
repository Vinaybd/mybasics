nums=[13,15,19,21,27]


for num in nums:
    if num % 2 == 0:
        print(num)
        break
else:
    print("Not found")