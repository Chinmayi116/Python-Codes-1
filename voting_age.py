# Program to validate name and age for voting eligibility

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    if age < 18:
        raise Exception("Not eligible to vote")

    print("Hello", name, "- You are eligible to vote")

except:
    print("Invalid input or age below 18")
