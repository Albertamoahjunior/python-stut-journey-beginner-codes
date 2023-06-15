#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ALBERT AMOAH JUNIOR
#
# Created:     25/05/2022
# Copyright:   (c) ALBERT AMOAH JUNIOR 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

temp = 0
find = 0
count = 0
i = 0
seth = [1,4,7,2,4,8,5]

while(count <= 6):
    temp = seth[i]
    if(temp > find):
        find = temp
    count += 1
    i +=1

print("The maximum is "+ str(find))
print(temp)