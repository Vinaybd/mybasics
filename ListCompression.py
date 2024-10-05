l=[1,2,3,4]

# this is one method that to append the list to dl
dl=[]

for num in l:
    dl.append(num*2)
    print(dl)

# list compression makes the code simple

dl=[num*2 for num in l]
print(dl)

# dl =[exp for item in collection]
dl =[item*2 for item in l]
print(dl)
dl =[item**2 for item in l]
print(dl)

l=[x for x in range(1,11)]
print(l)

#[exp for item in collection if item_condition] this the format to represnet
edl=[x**2 for x in l if x%2==0]
print(edl)


# we can perform this for strings
name =["vinay","vijay","vishwas"]
print(name)
dl=[item[1] for item in name]
print(dl)

# for dictinaries
names =["vinay","vijay","vishwas"]

d={name:len(name) for name in names }
print(d)

names =["vis","pus","sjdgdbsns"]

d={name:len(name) for name in names}
print(d)


#using dictionary we can print keyand value within for
cp={
    "Bengalore":45,
    "mysore":30,
    "Huballi":9,
    "Mangalore":20
}

lam = {key:value for key,value in cp.items() if value>10}

print(lam)