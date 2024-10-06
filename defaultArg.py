#default arguments = A default value for certain parameters
#                 default is used when the argumnet is omitted
#                 make your func more flexible,reduces # of arguments
#                 1.positional , 2.DEFAULT , 3.Keyword , 4.

def net_price(list_price,discount=0,tax=0.05):
    return list_price * (1-discount) * (1 + tax)

print(net_price(500,0,0.05))
print(net_price(500))
print(net_price(500,0.1,0))


# exaple
def add_item(item, item_list=[]):
    item_list.append(item)
    return item_list

# Calling the function
print(add_item("apple"))   # Output: ['apple']
print(add_item("banana"))  # Output: ['apple', 'banana'] (not what you might expect)



# exaple 2

def add_item_fixed(item, item_list=None):
    if item_list is None:
        item_list = []
    item_list.append(item)
    return item_list

# Calling the function
print(add_item_fixed("apple"))   # Output: ['apple']
print(add_item_fixed("banana"))  # Output: ['banana']
