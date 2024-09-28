#tuples and sets

gender =("male",)
# gender[0] = "un"
# print(gender[1])

sex = "nija"
new = gender +(sex,)
print(gender)
print(new)

a = ('2',)
b = 'z'
new = a + (b,)
print(new)

# sets
# sets are unique unordered and unindex then it will not allow duplicate values
#                Sets are useful for performing operation  like union,insertion,and difference
s1={20,13,45,2}
# s2 = set(1,2,3)
s2 = {1,2,3}
s3 =set() # empty set
print(s1)
print(s1|s2) #union
print(s1&s2) #intersection
print(s1-s2) #difference

s={1,2,3,4,5,}
# s.pop() #this func pop the first element
s.remove(2)#it will directly remove the second element
s.discard(3)#this will check if element their in set then remove that
s.add(6)
print(s)