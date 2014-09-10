def minimum_insurance(x):
    return 0.80 * x

amount = float(input("How much would it cost to replace your property? - "))
print("You should buy at least $", minimum_insurance(amount), "of insurance!")
