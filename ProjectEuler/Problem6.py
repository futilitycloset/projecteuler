#The sum of the squares of the first ten natural numbers is,
#1^2 + 2^2 + ... + 10^2 = 385

#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)^2 = 55^2 = 3025

#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import math

limit = 0
sumofsquares = 0
squareofsums = 0
firstnumber = 0
secondnumber = 0

while firstnumber < 101:
    sumofsquares = sumofsquares + firstnumber**2
    firstnumber = firstnumber + 1
    
while secondnumber < 101:
    squareofsums = squareofsums + secondnumber
    secondnumber = secondnumber + 1

squareofsums = squareofsums**2
    
solution = squareofsums - sumofsquares
print solution