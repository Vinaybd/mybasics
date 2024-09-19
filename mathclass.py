import math
# x=9
# print(math.pi)
# print(math.e)
# result=math.sqrt(x)
# # result = math.ceil(x) #round the value to nxt value
# result=math.floor(result) #round the valur to nearets back
 
# print(result)

#calculate radius

radius = float(input('Enter the radius of a circle:'))

circumference=2*math.pi*radius

# print(f"The circuference is : {circumference}")
print(f"The circuference is :{round(circumference,2)}")