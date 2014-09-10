print("For this game, you need to make up exactly $1 from change to win!\n")

pennies = int(input("How many pennies do you want? - "))
nickels = int(input("How many nickels do you want? - "))
dimes = int(input("How many dimes do you want? - "))
quarters = int(input("How many quarters do you want? - "))

total_cents = pennies + (5 * nickels) + (10 * dimes) + (25 * quarters)

if total_cents > 100:
    print("That's more than a dollar! You lose!")
elif total_cents < 100:
    print("That's less than a dollar! You lose!")
elif total_cents == 100:
    print("That's EXACTLY one dollar! YOU WIN!!")
else:
    print("There has been an error.")
