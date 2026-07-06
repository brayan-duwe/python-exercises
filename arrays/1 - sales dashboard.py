sales = [1500, 2000, 800, 3500, 1200]
total_sales = 0
higher_sale = sales[0]
lower_sale = sales[0]

for sale in sales:
    total_sales += sale
    if higher_sale < sale:
        higher_sale = sale
    if lower_sale > sale:
        lower_sale = sale

average = total_sales / len(sales)

print(f"Total sales: R${total_sales:.2f}")
print(f"Average: R$ {average:.2f}")
print(f"Higher sale: R${higher_sale:.2f} | Lower sale: R${lower_sale:.2f}")