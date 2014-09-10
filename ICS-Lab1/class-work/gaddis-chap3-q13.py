weight = float(input("Please enter the weight of the package in pounds - "))

if weight > 10:
    print("Your shipping charges are $", weight * 4.75)
elif weight > 6:
    print("Your shipping charges are $", weight * 4.00)
elif weight > 2:
    print("Your shipping charges are $", weight * 3.00)
elif weight > 0:
    print("Your shipping charges are $", weight * 1.50)
else:
    print("There has been an error.")
