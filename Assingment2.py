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

    print(rep)

integerRepresentation(17, 2)