def numberCheck(number, guess):
  if (number % 3 == 0 and number % 5 != 0 and guess.capitalize() == "Fizz"):
    print("Correct!")
  elif (number % 3 != 0 and number % 5 == 0 and guess.capitalize() == "Buzz"):
    print("Correct!")
  elif (number % 3 == 0 and number % 5 == 0 and guess.capitalize("FizzBuzz")):
    print("Correct!")
  elif (number % 3 != 0 and number % 5 != 0 and guess.capitalize() == "Normal"):
    print("Correct!")
  else:
    print("Incorrect! Game Over!")
    exit(1)

print("Hello and welcome to the FizzBuzz game!")

rules = input("Would you like to know the rules? (Y/N): ")

if (rules.capitalize() == "Y" or rules.capitalize() == "Yes"):
  print("Ok! I'll show you the rules.")
  print("The rules are:")
  print("1) The user, you, enters a number until which they'd like to play.")
  print("2) The computer will then print out the FizzBuzz sequence.")
  print("3)If the number is a multiple of 3, the user has to enter: Fizz.")
  print("4) If the number is a multiple of 5, the user has to enter: Buzz.")
  print("5) If the number is a mutliple of 5 and 3, the user will hae to enter: FizzBuzz.")
  print("6) If the number doesn't apply to any of the three, the user has to enter: Normal.")
  print("7) If the user enters the correct number until the number they chose, they win.")
  print("8) If they aren't able to complete the challenege correctly until the very end, they lose.")
  print("Also, if you'd like to end the game early, just enter: Stop.")

elif (rules.capitalize() == "N" or rules.capitalize() == "No"):
  print("Ok! I won't show you the rules.")

else:
  print("I don't understand this input! Please try again.")

gameNumber = input("Please enter a number until which you'd like to play: ")

playingNumber = 0

while (playingNumber != gameNumber):
  playingNumber += 1
  print(playingNumber)
  userGuess = input("Please enter your guess: ")
  numberCheck(playingNumber, userGuess)
