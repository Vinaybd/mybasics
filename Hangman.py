#Hangman in python
import random

words = ("apple","orange","banana","coconut","pineapple")

#dictionary of key :()
hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" O ",
                  "   ",
                  "   "),
               2:(" O ",
                  " | ",
                  "   "),
               3:(" O  ",
                  " | ",
                  "/\\"),
               4:(" O ",
                  " | ",
                  "/ /"),
               5:(" O ",
                  " | ",
                  "/\\" ),
               6:(" O  ",
                  " |  ",
                  "//\\" )}

# print(hangman_art)

def display_man(wrong_guesses):
    print("***************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("***************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    # print(hint)
    wrong_guesses = 3
    guessed_letters = set()
    is_running = True
    # print(answer)

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        display_answer(answer)
        guess = input("Enter a letter:").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input")
        # continue
    
    if guess in answer:
        for i in range(len(answer)):
            if answer[i] == guess:
                hint[i] = guess

# for line in hangman_art[6]:
#     print(line)

if __name__ == "__main__":
    main()