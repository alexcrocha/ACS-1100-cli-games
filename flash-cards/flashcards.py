import json

def load_capitals(file):
    with open(file, 'r') as f:
        return json.load(f)

data = load_capitals('me-capitals.json')

# initialize total as the length of the cards array
total = len(data["cards"])
# initialize score as 0
score = 0

for i in data["cards"]:
    guess = input(f'{i["q"]} > ')

    if guess.lower() == i["a"].lower():
        # increment score up one
        score += 1
        # interpolate score and total into the response
        print(f'Correct! Current score: {score}/{total}')
    else:
        print(f'Incorrect! The correct answer was {i["a"]}')
        print(f'Current score: {score}/{total}')

print(f'Thanks for playing! You scored: {score} out of {total} correct!')
if score == total:
    print('Amazing...')
elif score > total/2:
    print('Good work...')
else:
    print('You need practice...')


# Stretch Challenges:

# Use functions to organize your code.

    # Use a function to display the next question
        # This function might take the question and the answer as a parameter
        # And return True or False if the question was answered correctly
    # Write a function to display game messages
        # You might have a function to display a starting message
        # You might have a function to display an end game message