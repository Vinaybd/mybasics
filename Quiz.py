questions =("How many elements in the periodic table?:",
            "Which animal lays the largest eggs?:",
            "What is the most abundant gas in the Earths atmosphere?:",
            "How many bones are in the human body?:",
            "Which planet in the solar system is the hottest?:")

options =(("A.166","B.177","C.118","D.199"),
          ("A.Whale","B.Crocadile","C.Elephant","D.Ostrich"),
          ("A.Nitrogen","B.Oxygen","C.Carbon_Dioxide","D.Hydrogen"),
          ("A.206","B.207","C.208","D.209"),
          ("A.Mercury","B.Venus","C.Earth","D.Mars"))

answers=("C","D","A","A","B")
guesses =[]
score =0
question_num =0

for question in questions:
    print("--------------------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer")

    question_num +=1

print("--------------------------------")
print(" RESULTS  ")
print("--------------------------------")

print("answers :",end="")
for answer in answers:
    print(answer,end="")
print()

print("guesses :",end="")
for guess in guesses:
    print(guess,end="")
print()

score = int(score/len(questions)*100)
print(f"Your score is : {score}%")