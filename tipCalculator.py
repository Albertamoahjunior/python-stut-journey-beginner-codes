print("Welcome to the tip calculator")

bill = float(input("What was the total bill: "))
tipPercentage = int(input("What percentage tip will you like to give: "))

newbill = bill*(1 + tipPercentage/100)

totalPeople = int(input("How many people to split the bill: "))

billShare = round(newbill/totalPeople,2)

print(f"Each person should pay {billShare}$")