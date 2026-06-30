
smartphones_stock = 250

print("Number of smartphones in stock:", smartphones_stock)

while True: 
    option = input("Press (1) to add smartphones to stock or (2) to remove from stock: ")
    if option == "1":
        try:
            add_smartphones = input("Add smartphones \n Type the number: ")
            smartphones_stock += int(add_smartphones)
            break
        except ValueError:
            print("That wasn't an expected answer, try again.")

    elif option == "2":
        try:
            remove_smartphones = input("Remove smartphones \n Type the number: ")
            smartphones_stock -= int(remove_smartphones)
            break
        except ValueError:
                print("That wasn't an expected answer, try again.")

    else:
        print("That wasn't an expected answer, try again.")

print("Number of smartphones in stock:", smartphones_stock)