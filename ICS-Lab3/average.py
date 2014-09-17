file = open("numbers.txt","r")
number = file.readline()
total = int(number)
counter = 1

while number != "":
    number = file.readline()
    try:
        total += int(number)
        counter += 1
    except:
        pass

print("Cumulative average is:")
print(total / counter)


