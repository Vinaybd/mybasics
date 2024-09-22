name =(input("Enter the name :"))

phone_number = input("Enter your phone number :")

result = len(name)
result = name.find('v')
result = name.find("i")
result = name.rfind('v')
name = name.capitalize()
name = name.upper()
name = str(name.lower()) # we r using this just 
name = name.isdigit()  # it should hve only digits in i/p
name = name.isalpha()
phone_number = phone_number.count('-')
phone_number = phone_number.replace("-"," ")
print(name)
print(phone_number)