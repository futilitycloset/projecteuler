#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math
highpoint = 100000000
startpoint = 2520

def factoruntilcertaindivisor(startpoint, highpoint, targetdivisor):
    endpoint = highpoint + 1
    divisorlist = []
    for i in range(startpoint, endpoint):
        if i%targetdivisor == 0:
            divisorlist.append(i)
    return divisorlist
    
def commonbetweenlists(list1, list2):
    sharedlist = []
    for i in list1:
        if i in list2:
            sharedlist.append(i)
    return sharedlist

divisibleby11 = factoruntilcertaindivisor(startpoint, highpoint, 11)
divisibleby13 = factoruntilcertaindivisor(startpoint, highpoint, 13)
divisibleby14 = factoruntilcertaindivisor(startpoint, highpoint, 14)
divisibleby16 = factoruntilcertaindivisor(startpoint, highpoint, 16)
divisibleby17 = factoruntilcertaindivisor(startpoint, highpoint, 17)
divisibleby18 = factoruntilcertaindivisor(startpoint, highpoint, 18)
divisibleby19 = factoruntilcertaindivisor(startpoint, highpoint, 19)
divisibleby20 = factoruntilcertaindivisor(startpoint, highpoint, 20)

compare11and13 = commonbetweenlists(divisibleby11, divisibleby13)
comparesharedand14 = commonbetweenlists(compare11and13, divisibleby14)
comparesharedand16 = commonbetweenlists(comparesharedand14, divisibleby16)
comparesharedand17 = commonbetweenlists(comparesharedand16, divisibleby17)
comparesharedand18 = commonbetweenlists(comparesharedand17, divisibleby18)
comparesharedand19 = commonbetweenlists(comparesharedand18, divisibleby19)
comparesharedand20 = commonbetweenlists(comparesharedand19, divisibleby20)

print comparesharedand20[0]