from random import randint

roles = ["Bear", "Ninja", "Cowboy"]


def instructions():
    response = input("Would you like instructions? (Y/N) > ")
    if response.lower() == "y" or response.lower() == "yes":
        print(
            "\nBear, Ninja, Cowboy is an exciting game of strategy and skill! Pit your wit against the computer! Choose a player: Bear, Ninja, or Cowboy. The computer chooses a player. Bear eats Ninja, Ninja defeats Cowboy and cowboy shoots bear."
        )


def get_role():
    allowed_role = False
    while allowed_role == False:
        role = input("\nBear, Ninja, or Cowboy? > ")
        if role in roles:
            allowed_role = True
        else:
            print("Bear, Cowboy, and Ninja are the only allowed names")
    return role


def assign_role():
    return roles[randint(0, 2)]


def new_score(score, points):
    score = score + points
    print(f"You get {points} point. Your score is now {score}")
    return score


def end_game_stats(score):
    print(f"\nYour final score is {score}")
    if score == 0:
        print("It's like you never played")
    elif score > 0:
        print("At least you can do something right")
    else:
        print("SAD")


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
                print("You lose!", player, "is shot by", computer)
                score = new_score(score, -1)
            else:
                print("You win!", player, "eats", computer)
                score = new_score(score, 1)
        elif computer == "Bear":
            if player == "Cowboy":
                print("You win!", player, "shoots", computer)
                score = new_score(score, 1)
            else:
                print("You lose!", player, "is eaten by", computer)
                score = new_score(score, -1)
        elif computer == "Ninja":
            if player == "Cowboy":
                print("You lose!", player, "is defeated by", computer)
                score = new_score(score, -1)
            else:
                print("You win!", player, "eats", computer)
                score = new_score(score, 1)

        play_again = input("\nWould you like to play again? (Y/N) > ")
        if play_again.lower() == "y" or play_again.lower() == "yes":
            player = False
            computer = assign_role()
        else:
            break
    return score


print("Get ready to play Bear, Ninja, Cowboy!")
instructions()
final_score = start_game()
end_game_stats(final_score)
print("Game Over")

# Stretch Challenges
# Try these ideas:

# Comment your code! Pay close attention to the formatting and code blocks.
# Expand the game. Look up Rock, Paper, Scissors, Lizard, Spock. This is the same game but has five possible plays. Rock < Paper < Scissors < Lizard < Spock < Rock.
