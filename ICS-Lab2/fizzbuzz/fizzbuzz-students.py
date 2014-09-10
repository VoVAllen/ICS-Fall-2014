"""
The FizzBuzz Problem
====================

Write a program that prints the numbers from 1 to 100.
But for multiples of three, print “Fizz” instead of the number.
For the multiples of five, print “Buzz” instead of the number.
For numbers which are multiples of both three and five, print “FizzBuzz”.
"""

for x in range(1,101):
    if x % 3 == 0:
        print("Fizz",end="")
    if x % 5 == 0:
        print("Buzz",end="")
    elif x % 3 != 0 :
        print(x,end="")
    print()
