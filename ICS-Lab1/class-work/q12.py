number = int(input("How many packages are you buying? - "))
initial_price = number * 99

if number >= 100:
    print("Discount:", 0.4 * initial_price)
    print("Amount payable:", 0.6 * initial_price)
elif number >= 50:
    print("Discount:", 0.3 * initial_price)
    print("Amount payable:", 0.7 * initial_price)
elif number >= 20:
    print("Discount:", 0.2 * initial_price)
    print("Amount payable:", 0.8 * initial_price)
elif number >= 10:
    print("Discount:", 0.1 * initial_price)
    print("Amount payable:", 0.9 * initial_price)
elif number >= 0:
    print("Discount:", 0.0 * initial_price)
    print("Amount payable:", 1.0 * initial_price)
else:
    print("There has been an error.")
