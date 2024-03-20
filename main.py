from profit_margin_calculator import ProfitMarginCalculator

# Taking inputs from the user.
inv = int(input("Enter your total investment in Rupees: "))
rev = int(input("Enter your total revenue in Rupees: "))

# instantiating the object 
pm = ProfitMarginCalculator(investment = inv, revenue = rev)

# computing the profit margin

result = pm.compute()

print(result)


