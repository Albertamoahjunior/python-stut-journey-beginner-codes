row_1 = ["💛","💛","💛"]
row_2 = ["💛","💛","💛"]
row_3 = ["💛","💛","💛"]

mat = [row_1,row_2,row_3]

print(f"{row_1}\n{row_2}\n{row_3}\n")

hunt = input("Where do you want to hide your treasure ?: ")

horizontal = int(hunt[0])
vertical = int(hunt[1])

change = mat[horizontal-1]
change[vertical-1] = "X"

print(f"{row_1}\n{row_2}\n{row_3}\n")