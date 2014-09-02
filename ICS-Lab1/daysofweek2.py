number = int(input("Give me a number from 1 to 7 - "))

days = [ "Monday", "Tuesday", "Wednesday", "Thursday",
         "Friday", "Saturday", "Sunday" ]

try:
    print( number, "=", days[number - 1] )
except:
    print( "Hey, you cheated!" )

