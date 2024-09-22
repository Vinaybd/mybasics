# Validate user input exercise
# 1.user name is not more than 12 character
# 2.username must not contain spaces
# 3.username must not contain digits

username = input("Enter your username")
username.find("")
username.isalpha()

if len(username) > 12:
    print("Username should not exceed 12 characters")
elif not username.find("") == -1 :
    print("your username cant contain spaces")
elif not username.isalpha():
    print("Username should only contain alphabets")
else:
    print(f"Welcome {username}")
