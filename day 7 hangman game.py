HANGMAN 

import random

words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
         coyote crow deer dog donkey duck eagle ferret fox frog goat
         goose hawk lion lizard llama mole monkey moose mouse mule newt
         otter owl panda parrot pigeon python rabbit ram rat raven
         rhino salmon seal shark sheep skunk sloth snake spider
         stork swan tiger toad trout turkey turtle weasel whale wolf
         wombat zebra'''.split()

stages = [
          '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =======''' ,
        '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =======''' ,
    
        '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =======''',
    
        '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =======''',
    
        '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =======''',
    
        '''
      +---+
      |   |
      O   |
          |
          |
          |
    =======''',
    
        '''
      +---+
      |   |
          |
          |
          |
          |
    ======='''
    
    
]

chosen_word = random.choice(words)
lives = 6
print(f"pssst, the solution is {chosen_word}")

display = ["_" for _ in chosen_word]

eog = False

while not eog:
    guess = input("Guess a letter: ").lower()
    correct_guess = False

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            correct_guess = True

    if not correct_guess:
        lives -= 1
        if lives == 0:
            eog = True
            print("You lose")

    if "_" not in display:
        eog = True
        print("You win")

    print(" ".join(display))
    print(stages[lives])
