from random import randint
logo = """

                                                    d8b                                                   d8b                      
                                                d8P ?88                                                   ?88                      
                                             d888888P88b                                                   88b                     
 d888b8b  ?88   d8P d8888b .d888b,.d888b,      ?88'  888888b  d8888b      88bd88b ?88   d8P  88bd8b,d88b   888888b  d8888b  88bd88b
d8P' ?88  d88   88 d8b_,dP ?8b,   ?8b,         88P   88P `?8bd8b_,dP      88P' ?8bd88   88   88P'`?8P'?8b  88P `?8bd8b_,dP  88P'  `
88b  ,88b ?8(  d88 88b       `?8b   `?8b       88b  d88   88P88b         d88   88P?8(  d88  d88  d88  88P d88,  d8888b     d88     
`?88P'`88b`?88P'?8b`?888P'`?888P'`?888P'       `?8bd88'   88b`?888P'    d88'   88b`?88P'?8bd88' d88'  88bd88'`?88P'`?888P'd88'     
       )88                                                                                                                         
      ,88P                                                                                                                         
  `?8888P                                                                                                                          
           
"""

turn_easy = 10
turn_hard = 5

def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"The answer was {answer}. You got it.I don't expect that.Congratulations.")

def set_difficulty():
  level = input("Choose a difficulty.Do you play hard or easy? Type 'easy' or 'hard': ")
  if level == "easy":
    print("You would like to play 'easy'.Only have 10 attempt.")
    return turn_easy
  else:
    print("You would like to play 'hard'.Okaaaay only have 5 attempt. Good luck ")
    return turn_hard

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Hello, I hope you're fine today. \nWe're going to play a game with you. \nI have a number between 1 and 100 in my mind . \nGuess what?")
  answer = randint(1, 100)
  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"Wrong! You have {turns} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))

    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")
game()
