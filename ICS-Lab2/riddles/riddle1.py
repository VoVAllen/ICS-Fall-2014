"""
Riddle #1
=========

(1) What does this program do?
(2) Can you find a bug in the program? What input do you supply?
(3) Can you think of one way to make the program "better"?
"""

# HINT: xkcd 622

x = int(input("Enter a number - "))
output = [ 2 ]
number = 3

while number <= x:

    flag = True

    for element in output:
        if number % element == 0:
            flag = False
            break
        
    if flag == True:
        output.append(number)

    number += 1

print(output)  
