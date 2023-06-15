import random

names_string = input("Enter the names on the table separated by a comma")

names = names_string.split(",")

chosen_person = random.randint(0,len(names)-1)

print("The person to pay is " + names[chosen_person])