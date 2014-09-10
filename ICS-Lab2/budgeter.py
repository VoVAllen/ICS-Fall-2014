budget = float(input("What's your budget for the month? - "))
choice = "y"

count = 0
expenses = 0.0

while choice == "y" or choice == "Y":
    count += 1
    print("Please enter expense number", count, "- ", end="")
    expenses += float(input())
    choice = input("Enter another expense item? (Y/N) - ")

print("\nYour budget was:", budget)
print("Your expenses added up to:", expenses)

if budget - expenses >= 0.0:
    print("Congrats, you're under budget by $", (budget - expenses) )
else:
    print("Oh no! You're over budget by $", (expenses - budget) )
