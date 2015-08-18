#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

import math

finished = False
number = 18
primelist = [2, 3, 5, 7, 11, 13, 17]

def factor(input):
    endpoint = int(math.sqrt(input)) + 1
    lowdivisorlist = []
    highdivisorlist = []
    divisorlist = []

    for i in range(2, endpoint):
        if input%i == 0:
            lowdivisorlist.append(i)
                
    for i in lowdivisorlist:
        highdivisorlist.append(number/i)

    divisorlist = lowdivisorlist + highdivisorlist
    divisorlist.sort()
    return divisorlist
    
while finished == False:
    divisorlist = factor(number)
    if len(divisorlist) == 0:
        primelist.append(number)
    if len(primelist) == 10001:
        finished = True
    else:
        number = number + 1

print number
    
