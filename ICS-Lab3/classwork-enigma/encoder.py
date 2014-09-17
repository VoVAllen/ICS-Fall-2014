# Insert a message to be ciphered here
message = ""

# Insert an offset here
offset = 0

# Dictionary to perform the substitution cipher (uppercase only)
encoding = { "A": "", "B": "", "C": "", "D": "", "E": "",
             "F": "", "G": "", "H": "", "I": "", "J": "",
             "K": "", "L": "", "M": "", "N": "", "O": "",
             "P": "", "Q": "", "R": "", "S": "", "T": "",
             "U": "", "V": "", "W": "", "X": "", "Y": "",
             "Z": ""
           }

for letter in encoding.keys():
    temp = ord(letter) + offset
    if temp > 90:
        temp = 64 + temp % 90
    encoding[letter] = chr(temp)

"""
print(encoding)
"""

cipher = ""

for char in message:
    if ord(char) >= 65 and ord(char) <= 90:
        cipher += encoding[char]
    else:
        cipher += " "

print(message)
print(cipher)
