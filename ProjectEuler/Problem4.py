#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

#Find the largest palindrome made from the product of two 3-digit numbers.
import math

number = 998001
palindromelist = []
possiblesolutionlist = []
morepossiblesolutionlist = []

def palindrome(input):
    textnumber = str(input)
    length = len(textnumber)  
    if length == 5:
        if textnumber[0] == textnumber[length-1]:
            if textnumber[1] == textnumber[length-2]:
                palindromelist.append(input)
    if length == 6:
        if textnumber[0] == textnumber[length-1]:
            if textnumber[1] == textnumber[length-2]:
                if textnumber[2] == textnumber[length-3]:
                    palindromelist.append(input)

def factor(input):
    endpoint = int(math.sqrt(input)) + 1
    lowdivisorlist = []
    highdivisorlist = []
    for i in range(2, endpoint, 1):
        if input%i == 0:
            lowdivisorlist.append(i)
    for i in lowdivisorlist:
        highdivisorlist.append(input/i)
    divisorlist = lowdivisorlist + highdivisorlist
    divisorlist.sort()
    return divisorlist

while number > 1:
    palindrome(number)
    number = number - 1
    
for i in palindromelist:
    factorlist = factor(i)
    correctlengthlist = [x for x in factorlist if (99 < x < 1000)]
    if len(correctlengthlist) >= 2:
        possiblesolutionlist.append(i)

possiblesolutionlist.sort()

for i in possiblesolutionlist:
    maybeafactor = False
    newfactorlist = factor(i)
    for x in newfactorlist:
        if x > 99 and x < 1000:
            if i/x > 99 and i/x < 1000:
                maybeafactor = True
    if maybeafactor == True:
        morepossiblesolutionlist.append(i)

print morepossiblesolutionlist[-1]
                
        
    