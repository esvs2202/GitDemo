from profit_margin_calculator import ProfitMarginCalculator

# Taking inputs from the user.
inv = float(input("Enter your total investment in Rupees: "))
rev = float(input("Enter your total revenue in Rupees: "))
opex = float(input("Enter your operating expenditure in Rupees: "))

# instantiating the object 
pm = ProfitMarginCalculator(investment = inv, revenue = rev, operating_expenditure = opex)

# computing the profit margin

result = pm.compute()

print(result[0])
print(result[1])
print(result[2])


