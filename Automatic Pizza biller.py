print("Welcome to Elyon Pizza")

size = input("What size of pizza do you want? L, M or S: ")
wants_Pepperoni = input("Do you want pepperoni? Y or N: ")
wants_Extra_Cheese = input("Do you want extra cheese? Y or N:")

bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Please enter a valid size")

if wants_Pepperoni == "Y":
    if bill == 15:
        bill += 2
    else:
        bill += 3
if wants_Extra_Cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")