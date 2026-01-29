# Program to raise exception for negative number

try:
    n = int(input("Enter a number: "))
    if n < 0:
        # Raise exception if number is negative
        raise Exception("Number is negative")
    print("Valid number:", n)
except Exception as e:
    # Handle exception
    print("Error:", e)
