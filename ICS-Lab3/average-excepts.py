file = open("numbers.txt","r")
number = file.readline()

try:
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

except:
    print("The file appears to be empty!")






