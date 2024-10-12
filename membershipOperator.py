# membership operators = used to test whether a value is found in a sequence
#                      (string,list,tuple,set,or dictionary)
#                      1. in
#                      2. not in

word = "Vinay"



# if letter in word:
#     print(f"{letter} is present in the secret word")
# else:
#     print(f"{letter} is not present in the secret word")

while True:
    letter = input("Guess the letter in the secret word:")

    if letter not in word:
         print(f"{letter} is not present in the secret word")
         if letter == True:
            print("your guess is correct")
            break
    else:
        print(f"{letter} is present in the secret word")


    
