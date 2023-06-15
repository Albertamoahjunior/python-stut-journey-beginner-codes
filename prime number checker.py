def prime_checker(number):
    if number == 2:
        print(f"the number {number} is prime")
    elif number % 2 == 1:
        if number < 9:
           print("the number {number} is prime")
        elif number != 1 and number % 3 != 0 and number%5 != 0:
            print(f"the number {number} is prime")
        else:
            print(f"the number {number} is not prime")
    else:
        print(f"the number {number} is not prime")



n = int(input("Please enter your number to be numbered: "))

prime_checker(number = n)

def is_prime(check):
    is_prime = True
    divisor = 0
    if check > 2 and check != 0:
        for n in range(2,check):
            if check % n == 0:
                is_prime = False
                divisor = n
                break
        if is_prime:
            print("is prime")
        else:
            print(f"is not prime with divisor {divisor}")
    else:
        print("is prime")

is_prime(number)