#using a loop we can iterate
#suppose if the number is 5 then we can iterate from 0 to 5

num=[7,8,5,9]
print(num[1])
for i in num: 
    print(i)

#we will use iter function which converts list into iterator
#it.__next__() will give the next index value 
it=iter(num)
print(it.__next__())
print(it.__next__())
print(next(it))

class TopTen:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            value=self.num
            self.num+=1
            return value
        else:
            raise StopIteration
        
values=TopTen()
print(next(values))
for i in values:
    print(i)
          