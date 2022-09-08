import json
import random

deck = "me-capitals.json"

# Open the chosen file and return as a list so it can be randomized with random.shuffle
def load_deck(file):
    with open(file, "r") as f:
        return list(json.load(f)["cards"])


data = load_deck(deck)

# Randomize the order of questions and answers
def randomize_data(data):
    random.shuffle(data)

# Check if inputted answer is correct
def ask_question(question, answer):
    guess = input(f"{question} > ")
    if guess.lower() == answer.lower():
        return True
    else:
        return False

# End game score
def end_game(score, total):
    print(f"Thanks for playing! You scored: {score} out of {total} correct!")
    if score == total:
        print("Amazing...")
    elif score > total / 2:
        print("Good work...")
    else:
        print("You need practice...")

# Check if player wants to play again and load another game if yes
def play_again():
    result = input("Play Again? (Y/N) > ")
    if result.lower() == "y":
        start_game(data)

# Main game loop
def start_game(data):
    # initialize total as the length of the cards array
    total = len(data)
    # initialize score as 0
    score = 0
    randomize_data(data)

    for i in data:
        result = ask_question(i["q"], i["a"])

        if result == True:
            # increment score up one
            score += 1
            # interpolate score and total into the response
            print(f"Correct! Current score: {score}/{total}")
        else:
            print(f'Incorrect! The correct answer was {i["a"]}')
            print(f"Current score: {score}/{total}")

    end_game(score, total)
    play_again()


start_game(data)

print("Game Over")
