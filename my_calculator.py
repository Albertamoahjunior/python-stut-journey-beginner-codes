numbers = "2+4+2"

calculated = 0

def evaluate(numbers):
    global calculated
    if "^" in numbers:
        n = 0
        for operator in numbers:
            if operator == "^":
                calculated += int(numbers[n-1]) ** int(numbers[n+1])
            n += 1
    if "+" in numbers:
        n = 0
        for operator in numbers:
            if operator == "+":
                calculated += int(numbers[n-1])
                calculated += int(numbers[n+1])
            n += 1




evaluate(numbers)
print(calculated)