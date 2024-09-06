pos=-1

def search(list,n):

    l=0
    u=len(list)-1
    
    while l<=u:
        mid=(l+u)//2

        if list[mid]==n:
            globals()['pos']=mid
            return True
        elif list[mid]<n: 
            l=mid
        else:
            u=mid
    return False
list=[4,5,6,79,2,67,87,4,533,77,33,7878,6554]
n=6554

if search(list,n):
   print("Found at",pos+1)
else:
   print("Not Found")
