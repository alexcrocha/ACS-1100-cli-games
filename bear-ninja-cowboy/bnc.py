from random import randint

name = input("Greetings, what is your name? > ")
print("Greetings", name)

roles = ["Bear", "Ninja", "Cowboy"]

computer = roles[randint(0,2)]

player = False

while player == False:

  player = input("Bear, Ninja, or Cowboy? > ")

  if computer == player:
      print("DRAW!")
  elif computer == "Cowboy":
    if player == "Bear":
      print("You lose!", computer, "shoots", player)
    else:
      print("You win!", player, "defeats", computer)
  elif computer == "Bear":
    if player == "Cowboy":
      print("You win!", player, "is eaten by", computer)
    else:
      print("You lose!", player, "is eaten by", computer)
  elif computer == "Ninja":
    if player == "Cowboy":
      print("You lose!", player, "is defeated by", computer)
    else:
      print("You win!", player, "eats", computer)

  play_again = input("Would you like to play again? (Y/N) > ")
  if play_again.lower() == 'y' or play_again.lower() == 'yes':
    player = False
    computer = roles[randint(0,2)]
  else:
    break
