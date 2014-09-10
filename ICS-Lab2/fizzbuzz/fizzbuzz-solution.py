# One of many FizzBuzz solutions

"""
More information about FizzBuzz (and about 1 bajillion solutions) here:
http://c2.com/cgi/wiki?FizzBuzzTest

There are tons of different solutions in Python and many, many other languages
"""

for x in range(1,101):
        s = ""
        if x % 3 == 0:
                s += "Fizz"
        if x % 5 == 0:
                s += "Buzz"
        if s == "":
                s = x
        print(s)
