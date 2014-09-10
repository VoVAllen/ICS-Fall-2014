bugs_collected = 0

for i in range(5):
    print( "DAY " + str(i+1) + ": ", end="")
    bugs_collected += int(input("How many bugs did you collect? - "))

print( "In total, over the 5 days, you collected", bugs_collected, "bugs!" )
