def state_tax(x):
    return 0.05 * x

def county_tax(x):
    return 0.025 * x

def total_tax(x):
    return state_tax(x) + county_tax(x)


amount = float(input("Enter some amount of money: "))

print("State Tax = $", state_tax(amount), sep='')
print("County Tax = $", county_tax(amount), sep='')
print("Total Sales Tax = $", total_tax(amount), sep='')
print("Total Sale Amount = $", amount + total_tax(amount), sep='')
