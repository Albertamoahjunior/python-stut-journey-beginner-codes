height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight/height**2

if bmi <= 18.5:
    print(f"Your body mass index is {bmi} and you are underweight")
elif bmi < 25:
    print(f"Your body mass index is {bmi} and you are normal weight")
elif bmi < 30:
    print(f"Your body mass index is {bmi} and you are  overweight")
elif bmi < 35:
    print(f"Your body mass index is {bmi} and you are overweight")
else:
    print(f"Your body mass index is {bmi} and you are clinically obesed")