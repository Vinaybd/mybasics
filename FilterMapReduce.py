from functools import reduce



nums =[3,2,6,8,4,6,2,9]

evens=list(filter(lambda n: n%2==0,nums))

doubles=list(map(lambda n: n*2,evens))

sum=reduce(lambda a,b: a+b,doubles)
print(evens)
print(sum)

min=list(filter(lambda a:a%4==0,nums))

print(min)