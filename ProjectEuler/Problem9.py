#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

import math

perfectsquarelist = []
number = 1

while number < math.sqrt(1000):
	perfectsquarelist.append(number**2)
	number += 1






"""a = 3
b = 4
finished = False

while b < 1000 and finished == False:
	csquared = (a*a + b*b)
	print "csquared is " + str(csquared)
	if csquared%(csquared**.5) == 0:
		print "csquared is a perfect square"
		if int(a + b + csquared**.5) == 1000:
			print "sum is 1000"
			finished = True
			break
	b += 1

if finished == False:
	csquared = (a*a + b*b)
	print "csquared is " + str(csquared)
	if csquared%(csquared**.5) == 0:
		print "csquared is a perfect square"
		if int(a + b + csquared**.5) == 1000:
			print "sum is 1000"
			finished = True
			break
	a += 1

print "a = " + str(a) 
print "b = " + str(b) 
print "c = " + str(int(csquared**.5))
print "a x b x c = " + str(int(a*b*(csquared**.5)))"""