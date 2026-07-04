full_name = input("Type your full name: ").split()
email = input("Type your email: ").lower().strip()

first_name = full_name[0].title()

print(f"The user has been registered. Name: {first_name}. Email: {email}.")