filename = input("Please give us a file name: ")

try:
    file = open(filename,"r")
    line = file.readline()
    counter = 1

    while line != "" and counter < 6:
        print(line, end="")
        line = file.readline()
        counter += 1

    file.close()

except:
    print("Probably an invalid file name... ")



