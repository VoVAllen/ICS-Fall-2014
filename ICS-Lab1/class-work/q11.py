books = int(input("How many books did you buy this month? - "))

if books >= 8:
    print("Serendipity Books awards you 60 points!")
elif books >= 6:
    print("Serendipity Books awards you 30 points!")
elif books >= 4:
    print("Serendipity Books awards you 15 points!")
elif books >= 2:
    print("Serendipity Books awards you 5 points!")
elif books >= 0:
    print("Serendipity Books awards you no points!")
else:
    print("There has been an error.")
