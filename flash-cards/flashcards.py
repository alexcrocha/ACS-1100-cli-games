import json

def load_capitals(file):
    with open(file, 'r') as f:
        return json.load(f)

data = load_capitals('me-capitals.json')


def ask_question(question, answer):
    guess = input(f'{question} > ')

    if guess.lower() == answer.lower():
        return True
    else:
        return False

def end_game(score, total):
    print(f'Thanks for playing! You scored: {score} out of {total} correct!')
    if score == total:
        print('Amazing...')
    elif score > total/2:
        print('Good work...')
    else:
        print('You need practice...')

def play_again():
    result = input('Play Again? (Y/N) > ')
    if result.lower() == 'y':
        start_game(data)

def start_game(data):
    # initialize total as the length of the cards array
    total = len(data["cards"])
    # initialize score as 0
    score = 0

    for i in data["cards"]:
        result = ask_question(i["q"], i["a"])

        if result == True:
            # increment score up one
            score += 1
            # interpolate score and total into the response
            print(f'Correct! Current score: {score}/{total}')
        else:
            print(f'Incorrect! The correct answer was {i["a"]}')
            print(f'Current score: {score}/{total}')

    end_game(score,total)
    play_again()

start_game(data)

print('Game Over')


# Stretch Challenges:

# Randomize the order of questions.
# Keep playing until the player gets all the questions right at least once.
# Keep playing until the player answers correctly 10 in a row.
# Create various data files that are different sets of questions and let people pick which one they want to do.
# Let people enter their own cards and save those as libraries of questions and answers.