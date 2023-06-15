import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper ='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: "))
computer_choice = random.randint(0,2)
computer_choice_range = [rock,paper,scissors]
if user_choice == 0 and computer_choice == 0:
    print(f"Your choice: \n {rock}\n Computer Choice:\n")
    print(computer_choice_range[computer_choice])
    print("You draw")
elif user_choice == 0 and computer_choice == 1:
    print(f"Your choice: \n {rock}\n Computer Choice:\n")
    print(computer_choice_range[computer_choice])
    print("You lose")
elif user_choice == 0 and computer_choice == 2:
    print(f"Your choice: \n {rock}\n Computer Choice:\n")
    print(computer_choice_range[computer_choice])
    print("You win")
elif user_choice == 1 and computer_choice == 1:
    print(f"Your choice: \n {paper}\n Computer Choice:\n")
    print(computer_choice_range[computer_choice])
    print("You draw")
elif user_choice == 1 and computer_choice == 2:
    print(f"Your choice: \n {paper}\n Computer Choice:\n")
    print(computer_choice_range[computer_choice])
    print("You lose")
elif user_choice == 1 and computer_choice == 0:
    print(f"Your choice: \n {paper}\n Computer Choice:\n")
    print(computer_choice_range[computer_choice])
    print("You win")
elif user_choice == 2 and computer_choice == 2:
    print(f"Your choice: \n {scissors}\n Computer Choice:\n")
    print(computer_choice_range[computer_choice])
    print("You draw")
elif user_choice == 2 and computer_choice == 1:
    print(f"Your choice: \n {scissors}\n Computer Choice:\n")
    print(computer_choice_range[computer_choice])
    print("You win")
else:
    print(f"Your choice: \n {scissors}\n Computer Choice:\n")
    print(computer_choice_range[computer_choice])
    print("You loose")
