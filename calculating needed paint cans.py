import math
test_h = int(input("Enter the height of the area: "))
test_w = int(input("Enter the width of the area: "))

coverage = 5

def paint_calc(height, width, cover):
    cans_needed = height * width / coverage
    print(math.ceil(cans_needed))

paint_calc(height = test_h, width = test_w, cover = coverage)