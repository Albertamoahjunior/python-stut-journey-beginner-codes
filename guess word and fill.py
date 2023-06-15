import random
from hangman_art import logo,stages
from hangman_words import word_list

hangman = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


print(logo)
choice = random.randint(0, len(word_list)-1)
choice_word = word_list[choice]

print(choice_word)

word = []
#Creation of blank spaces
for letter in choice_word:
    word.append("_")
print(word)

#replacing the blank spaces
lives = 7
while "_" in word:
    guess = input("Guess a letter: ").lower()

    for n in range(0, len(choice_word)):
        if guess == choice_word[n]:
            word[n] = guess
    if guess not in choice_word:
        lives -= 1
        print(stages[lives])
    if lives <= 0:
        break

    print(word)

i = 0
for n in word:
    if n == "_":
        print("You lost")
        break
    if n != "_":
        if i < len(word)-1:
            pass
        else:
            print("You win")
    i += 1
