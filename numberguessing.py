
import random


user_life = 3
number = 10

secret_number = random.randint(0, number)

while user_life > 0:
  user_input = int(
    input(f"Guess the number between 0 and {number} inclusively: "))
  if user_input != secret_number:
    if secret_number % 2 != 0:
      clues1 = [
        f"The number is the cube root of {secret_number ** 3}",
        f"The number is the square root of {secret_number ** 2}",
        "The number is odd"
      ]
      print(random.choice(clues1))
    else:
      clues2 = [
        "The number is divisible by two",
        f"The number is twice as big as {secret_number // 2}",
        f"The number is the square root of {secret_number ** 2}"
      ]
      print(random.choice(clues2))
    user_life -= 1
  else:
    match user_life:
      case 3:
        print("\nWhat a guess!")
      case 2:
        print("\nGenius!")
      case 1:
        print("\nHelpful clues?")
      case 0:
        print("\nPay attention to the clues")
    break

print(f"Your score is {user_life}")

if user_input == secret_number:
  pass
else:
  print(f"The secret number was {secret_number}")
