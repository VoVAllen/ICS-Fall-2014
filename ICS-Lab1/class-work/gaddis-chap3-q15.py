seconds = int(input("Please enter a number of seconds - "))

if seconds >= 86400:
    print( "That's", int(seconds/86400), "days +", (seconds % 86400), "seconds" )
elif seconds >= 3600:
    print( "That's", int(seconds/3600), "hours +", (seconds % 3600), "seconds" )
elif seconds >= 60:
    print( "That's", int(seconds/60), "minutes +", (seconds % 60), "seconds" )
else:
    print( "That's", seconds, "seconds" )
