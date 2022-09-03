import json

with open('me-capitals.json', 'r') as f:
    data = json.load(f)

# initialize total as the length of the cards array
total = json.load(f)
# initialize score as 0
score = 0

for i in data["cards"]:
    guess = input(i["q"] + " > ")

    if guess.lower() == i["a"].lower():
        # increment score up one
        score += 1
        # interpolate score and total into the response
        print(f"Correct! Current score: {score}/{total}")
    else:
        print("Incorrect! The correct answer was", i["a"])
        print(f"Current score: {score}/{total}")


# Stretch Challenges:
# f-strings - Can you use f-strings to change how we do string interpolations throughout this program?
# End game message - print a message when the game ends, something like: "Thanks for playing! You scored: 4 out five correct!"
# To find the number of questions len() to count the cards array.
# Modify the message based on the score:
# Less than half correct: "You need practice..."
# More than half correct: "Good work..."
# All correct: "Amazing..."
# Use functions to organize your code.
# Use a function to read the data file.
# This function might take the file path as a parameter
# And return the data that was loaded
# Use a function to display the next question
# This function might take the question and the answer as a parameter
# And return True or False if the question was answered correctly
# Write a function to display game messages
# You might have a function to display a starting message
# You might have a function to display an end game message