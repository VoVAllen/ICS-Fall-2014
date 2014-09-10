"""
Riddle #2
=========

(1) What does this program do?
(2) Can you find at one way to "break" the program? What input do you supply?
(3) Does the while loop in func() always terminate? Why or why not?
"""

# HINT: xkcd 710

def func(x):
    
    chain = []
    if x == 1:
        return [4, 2, 1]
    
    while x != 1:
        chain.append(x)
        if x % 2 == 0:
            x //= 2
        else:
            x *= 3
            x += 1

    chain.append(x)
    return chain

n = int(input("Enter a number - "))
print(func(n))
