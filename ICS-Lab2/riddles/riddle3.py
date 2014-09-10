"""
Riddle #3
=========

CAUTION: This program takes a LONG time to run. Please be patient!

(1) What does this program do?
(2) What does this mean for the US Dollar (cents, nickels, dimes, quarters)? What assumption does this finding depend upon?
(3) What's a reasonable estimate of how many calculations this script performed?
"""

# HINT: Think about money, and how many coins you need to pay for something
# HINT #2: Look at the bottom of the program

w = 1
x = w+1
y = x+1
z = y+1

coins = [w,x,y,z]
numbers = range(1,100)

coinsrequired = []
avgcoinsrequired = {}

while x<=99:
    print("Still running... ",x+1,"%",sep="")
    y = x+1
    while y<=99:
        z = y+1
        while z <=99:
            coins = [w,x,y,z]
            coinsrequired = []
            for i in numbers:
                coincounter = 0
                while i >= z:
                    i -= z
                    coincounter += 1
                while i >= y:
                    i -= y
                    coincounter += 1
                while i >= x:
                    i -= x
                    coincounter += 1
                while i >= w:
                    i -= w
                    coincounter += 1
                    
                coinsrequired.append(coincounter)
                avgcoinsrequired[str(coins)] = float( sum(coinsrequired) ) / float( len(coinsrequired) )
            z += 1
        y += 1
    x += 1

for element in avgcoinsrequired.keys():
    if avgcoinsrequired[element] < 4.15:
        print (element, "->", avgcoinsrequired[element])



USDollar = [1,5,10,25]
coinsreq = []
for i in range(1,100):
    coincounter = 0
    while i >= 25:
        i -= 25
        coincounter += 1
    while i >= 10:
        i -= 10
        coincounter += 1
    while i >= 5:
        i -= 5
        coincounter += 1
    while i >= 1:
        i -= 1
        coincounter += 1
    coinsreq.append(coincounter)
    avgcoinsreq = float( sum(coinsreq) ) / float( len(coinsreq) )
    
print (USDollar, "->", avgcoinsreq)
