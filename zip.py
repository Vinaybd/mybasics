names=("vinay","kiran","manju")
comps=("Apple","Dell","MS")

zipped=list(zip(names,comps)) #list gives the list of names 
zipped=set(zip(names,comps))
zipped=dict(zip(names,comps))          #we can also use set ,dict func
print(zipped)

zipped=zip(names,comps)

for (a,b) in zipped:
    print(a,b)