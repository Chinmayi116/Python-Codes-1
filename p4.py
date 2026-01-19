def calculate_exp(name, *exp):
    total = sum(exp)
    print("Name:", name)
    print("Exp:", total)

name = input("Enter your name: ")

# Taking multiple values as comma-separated input
exp_input = input("Enter your exp (comma separated): ")

# Convert string input to integers without map()
exp = tuple(int(x) for x in exp_input.split(","))

calculate_exp(name, *exp)
