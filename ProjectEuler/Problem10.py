#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

import math

startpoint = 5
lowdivisorlist = []
highdivisorlist = []
primelist = [2, 3]

def factor(tobefactored):
    endpoint = int(math.sqrt(tobefactored)) + 1
    lowdivisorlist = []
    highdivisorlist = []
    divisorlist = []

    for i in range(2, endpoint):
        if tobefactored%i == 0:
            lowdivisorlist.append(i)
                
    for i in lowdivisorlist:
        highdivisorlist.append(tobefactored/i)

    divisorlist = lowdivisorlist + highdivisorlist
    divisorlist.sort()
    return divisorlist

while startpoint < 2000000:
	divisorlist = factor(startpoint)
	if len(divisorlist) == 0:
		primelist.append(startpoint)
	startpoint += 2

print sum(primelist)
    
"""while startpoint < 2000000:
	divisorlist = factor(startpoint)
	for i in divisorlist:
		newdivisorlist = factor(i)
  		if len(newdivisorlist) == 0:
			if i not in primelist:
				primelist.append(i)
	startpoint += 1"""

