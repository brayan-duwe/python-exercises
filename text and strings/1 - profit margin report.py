import locale
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

revenue = 45_000
costs = 23_000

profit = revenue - costs
margin = profit / revenue * 100

profit_formatted = locale.currency(profit, grouping=True)

print(f"Profit: {profit_formatted} | Margin: {round(margin)}%")

# same result

print(f"Profit: R$ {profit:,.2f} | Margin: {margin:.0%}")
