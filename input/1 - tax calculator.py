tax = 0.15

value = input("Type the value: ")

value = value.replace("R$", "").replace(".", "").replace(",", ".")
value = float(value)
final_value = value * tax

print(f"The tax is: R${final_value:.2f}")