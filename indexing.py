# indexing = accesing elements of a sequence using [] (indexing operator)
#           [start : end : step]  [::2]-2 is step value

credit_number = "1234-5678-9123"
print(credit_number[0])
print(credit_number[0:4])
print(credit_number[4:])
print(credit_number[0:])
print(credit_number[-1]) #-1 says it takes the value from reverse order
print(credit_number[-4])
print(credit_number[10:])
print(credit_number[::2]) # :: this we will use bcs whenwe need step value
last_digit = credit_number[-4:]
print(f"xxxx-xxxx-{last_digit}")

credit_number = credit_number[::-1] #this will reverse the string
print(credit_number)

credit_number = credit_number.split()
print(credit_number)