#-------------------------------------------------------------------------------
# Name:        Assignment
# Purpose:
#
# Author:      ALBERT AMOAH JUNIOR
#
# Created:     11/05/2022
# Copyright:   (c) ALBERT AMOAH JUNIOR 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def euclideanAlgorithm(a,b):
    x = a
    y = b
    r = 0
    while y != 0:
        r = x%y
        x = y
        y = r

    print("the gcd of the integers is "+ str(x))

euclideanAlgorithm(2, 3)
