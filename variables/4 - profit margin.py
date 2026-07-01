revenue = 15_000
fixed_costs = 5000
taxes_percentage = 15

taxes_value = revenue * (taxes_percentage / 100)
profit = revenue - fixed_costs - taxes_value
profit_margin = profit / revenue


print("Taxes value: R$", taxes_value)
print("Profit: R$", profit)
print("Profit margin: ", profit_margin)

target_reached = profit_margin > 0.3
print("Target reached?", target_reached)
