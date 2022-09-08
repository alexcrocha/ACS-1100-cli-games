from random import randint

roles = ["Bear", "Ninja", "Cowboy"]

# Ask for instructions when the game loads for the first time
def instructions():
    response = input("Would you like instructions? (Y/N) > ")
    if response.lower() == "y" or response.lower() == "yes":
        print(
            "\nBear, Ninja, Cowboy. Pick one.\nBear eats Ninja, Ninja defeats Cowboy, and Cowboy shoots Bear.\nMake your choice and be quick about it - you will lose all the same."
        )

# Ask for role selection until an allowed role is selected
def get_role():
    allowed_role = False
    while allowed_role == False:
        # I want to make sure only the first character is capitalized
        role = input("\nBear, Ninja, or Cowboy? > ").lower().capitalize()
        # Check if inputted role exists
        if role in roles:
            allowed_role = True
        else:
            print("Bear, Cowboy, and Ninja are the only allowed names")
    return role


def assign_role():
    return roles[randint(0, 2)]

# Calculates score and shows score progression
def new_score(score, points):
    score += points
    print(f"You get {points} point. Your score is now {score}")
    return score

# Show end game stats
def end_game_stats(score):
    print(f"\nYour final score is {score}")
    if score == 0:
        print("It's like you never even played")
    elif score > 0:
        print("At least you can do something right")
    else:
        print("SAD")

# Main game loop
def start_game():
    player = False
    score = 0
    while player == False:

        computer = assign_role()
        player = get_role()

        if computer == player:
            print("DRAW!")
        elif computer == "Cowboy":
            if player == "Bear":
                print("You lose!", player, "is shot by", computer, "- Ouch!")
                score = new_score(score, -1)
            else:
                print("You win!", player, "defeats", computer, "- Woosh!")
                score = new_score(score, 1)
        elif computer == "Bear":
            if player == "Cowboy":
                print("You win!", player, "shoots", computer, "- Ouch!")
                score = new_score(score, 1)
            else:
                print("You lose!", player, "is eaten by", computer, "- Yum!")
                score = new_score(score, -1)
        elif computer == "Ninja":
            if player == "Cowboy":
                print("You lose!", player, "is defeated by", computer, "- Woosh!")
                score = new_score(score, -1)
            else:
                print("You win!", player, "eats", computer, "- Yum!")
                score = new_score(score, 1)

        play_again = input("\nWould you like to play again? (Y/N) > ")
        if play_again.lower() == "y" or play_again.lower() == "yes":
            player = False
            computer = assign_role()
        else:
            print('Out with you!')
            break
    return score


print("Get ready to play Bear, Ninja, Cowboy!")
instructions()
final_score = start_game()
end_game_stats(final_score)
print("Game Over")
