
#method for using euclidean algorithm
def euclideanAlgorithm(a,b):
    x = a
    y = b
    r = 0
    while y != 0:
        r = x%y
        x = y
        y = r

    print("the gcd of the integers is "+ str(x))


#method for integer representation
def integerRepresentation(a,b):
    x = a
    rep = []

    while x!= 0:
        r = x % b
        rep.append(r)
        x = int(x/b)

    rep.reverse()
    return rep



#Method for adding integers
def additionOfIntegers(a,b):
    added = 0
    great = 0
    carry = 0
    newInteger = []
    firstInteger = integerRepresentation(a,2)
    secondInteger = integerRepresentation(b,2)

    n = len(firstInteger)


    while n != 0:
        added = firstInteger[n-1] + secondInteger[n-1] + carry
        if(added >= 2):
            great = added % 2
            carry = added/2
            newInteger.append(int(great))
        else:
            newInteger.append(int(added))
        n -= 1
    newInteger.append(int(carry))

    print(newInteger)



euclideanAlgorithm(10,20)
print(integerRepresentation(6,2))
additionOfIntegers(4,5)