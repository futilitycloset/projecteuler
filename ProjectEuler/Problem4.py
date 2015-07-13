#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

#Find the largest palindrome made from the product of two 3-digit numbers.
import math

number = 998001
palindromelist = []
possiblesolutionlist = []

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

print palindromelist

for i in palindromelist:
    staytrue = True
    factorlist = factor(i)
    for i in factorlist:
        if i < 100 or i > 999:
            factorlist.remove(i)
    print factorlist