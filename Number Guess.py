import random

print("Welcome to the number Guessing Game!")
print("I am thinking of a number between 1 and 100")

number = random.randint(1,101)
end = 0

difficulty = input("Choose a difficulty. Type easy or hard: ")
if difficulty == "easy":
    count = 10
elif difficulty == "hard":
    count = 5
else:
    print("Invalid input")

while end < count:
        print(f"You have {count - end} attempts remaining to make a guess")
        guess = int(input("Make a guess: "))
        if guess == number:
            print("You win")
            break
        elif guess < number:
            print("The number is too low")
        else:
            print("Your number is too high")
        end += 1
if end > count:
    print(f"You have used up all your guesses")


