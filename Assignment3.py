#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ALBERT AMOAH JUNIOR
#
# Created:     11/05/2022
# Copyright:   (c) ALBERT AMOAH JUNIOR 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def integerRepresentation(a,b):
    x = a
    rep = []

    while x!= 0:
        r = x % b
        rep.append(r)
        x = int(x/b)

    rep.reverse()

    return rep



def additionOfIntegers(a,b):
    added = 0
    great = 0
    carry = 0
    newInteger = []
    firstInteger = integerRepresentation(a,2)
    secondInteger = integerRepresentation(b,2)

    n = len(firstInteger)
    #r = 4

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
    #print(n)
    #print(firstInteger)
    #print(secondInteger)
    print(newInteger)

additionOfIntegers(4,5)


