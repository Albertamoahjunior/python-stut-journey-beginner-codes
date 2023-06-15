a = input("Enter your number: ")
b = input("Enter another number: ")

print("a: " + str(a))
print("b: " + str(b))

c = a
a = b
b = c

print("After switch")

print("a: " + str(a))
print("b: " + str(b))