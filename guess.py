# Program for number guessing game using exceptions

num = 7   # Number to guess

while True:
    try:
        g = int(input("Guess the number: "))
        if g > num:
            raise ValueError("Value too large")
        elif g < num:
            raise ValueError("Value too small")
        else:
            print("Correct Guess!")
            break
    except ValueError as e:
        print("Try again:", e)
