file = open("numbers.txt","r")
number = file.readline()

while number != "":
    print(number, end="")
    number = file.readline()
