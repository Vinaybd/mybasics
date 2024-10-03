import random

options =("rock","paper","scissors")
player = None
computer = random.choice(options)

while player not in options:
    player = input("Enter your choice (rock, paper,  scissors): ")


print(f"player: {player}")
print(f"computer: {computer}")

