#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

perfectsquarelist = []
Asquarelist = []
Bsquarelist = []
triplelist = []
number = 1

while number < 1000:
	perfectsquarelist.append(number**2)
	number += 1

number = 1

while number < 333:
	Asquarelist.append(number**2)
	number += 1

number = 1

while number < 500:
	Bsquarelist.append(number**2)
	number += 1

for a in Asquarelist:
	for b in Bsquarelist:
		if b>a:
			c = b+a
			if c in perfectsquarelist:
				if a**.5 + b**.5 + c**.5 == 1000:
					a = a**.5
					b = b**.5
					c = c**.5
					print "a= " + str(a)
					print "b= " + str(b)
					print "c= " + str(c)
					print "product is " + str(a*b*c)

"""for a in perfectsquarelist:
	for b in perfectsquarelist:
		c = a+b
		if c in perfectsquarelist:
			triplelist.append(tuple([a,b,c]))"""

"""for i in perfectsquarelist:
	currentfirst = i
	firstsum = 0
	secondsum = 0
	for i in perfectsquarelist:
		if i != currentfirst:
			firstsum = currentfirst + 1
				for i in perfectsquarelist:"""

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