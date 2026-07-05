
while True:
    try: 
        revenue_store_a = float(input("Type the first revenue: "))
    except (ValueError, KeyboardInterrupt):
        print("Invalid option, try again.")
    try: 
        revenue_store_b = float(input("Type the second revenue: "))
    except (ValueError, KeyboardInterrupt):
        print("Invalid option, try again.")
    total_revenue = revenue_store_a + revenue_store_b
    average = total_revenue / 2
    print(f"The total revenue is R${total_revenue:,.2f}, and the average R${average:,.2f}.")

    break
