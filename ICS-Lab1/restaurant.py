meal = int(input("Please enter the price of a meal - "))
tip = 0.18 * meal
tax = 0.07 * meal
print( "You need to tip:", tip )
print( "Sales Tax is:", tax )
print( "Total amount is:", meal + tip + tax )


