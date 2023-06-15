import random

word_list = ["ardvark","mouse","goat"]

choice = random.randint(0, len(word_list)-1)
choice_word = word_list[choice]
print(choice)

guess = input("Guess a letter: ")
print(guess)

for letter in choice_word:
    if guess.lower() == letter:
        print("right")
    else:
        print("wrong")