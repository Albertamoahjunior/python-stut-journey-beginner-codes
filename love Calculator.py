print("Welcome to love calculator")

firstName = (input("Enter your name: ")).lower()
secondName = (input("Enter their name: ")).lower()

count_for_t = 0
count_for_r = 0
count_for_u = 0
count_for_e = 0

count_for_l = 0
count_for_o = 0
count_for_v = 0
count_for_le = 0

#for first name
count_for_t += firstName.count("t")
count_for_r += firstName.count("r")
count_for_u += firstName.count("u")
count_for_e += firstName.count("e")

count_for_l += firstName.count("l")
count_for_o += firstName.count("o")
count_for_v += firstName.count("v")
count_for_le += firstName.count("e")


#for second name
count_for_t += secondName.count("t")
count_for_r += secondName.count("r")
count_for_u += secondName.count("u")
count_for_e += secondName.count("e")

count_for_l += secondName.count("l")
count_for_o += secondName.count("o")
count_for_v += secondName.count("v")
count_for_e += secondName.count("e")

for_true = count_for_t + count_for_r + count_for_u + count_for_e
for_love = count_for_l + count_for_o + count_for_v + count_for_le

final_score = str(for_true) + str(for_love)

compatible_score = int(final_score)

if compatible_score < 10 or compatible_score > 90:
    print(f"Your score is {compatible_score} and you are like coke and menthos")
elif compatible_score > 40 and compatible_score < 50:
    print(f"Your score is {compatible_score} and you are well together")
else:
    print(f"Your score is {compatible_score}")
