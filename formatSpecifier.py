# format specifier ={value:flags} format a value based on what
#                                 flags are inserted
#  a format specifier is a placeholder in a string that defines how a -
#  -particular variable's value should be formatted when converting it to a string. They are commonly used in languages like C, Python, and Java for output formatting

price1 = 3.1415
price2 = -986234.45
price3 = 12.34

print(f"Price 1 is ${price1:.3f}") #.3f will give the 3 points after decimal point
print(f"Price 2 is ${price2:.3f}") #this format speifier uses while converting varible ,string
print(f"Price 3 is ${price3:.3f}")
print(f"Price 1 is ${price1:10}") # precedes empty space for value
print(f"print 2 is ${price2:010}")#fill the empty space with precedence 0
print(f"print 3 is ${price3:<10}")
print(f"print 1 is ${price1:>10}")
print(f"price 2 is ${price2:^10}")
print(f"print 2 is ${price2:,}")
print(f"print 2 is ${price2:+,.2f}")
print(f"price 1 is ${price1:+,.2f}")
