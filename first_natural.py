# Program to print first 20 natural numbers and stop using exception

class StopIteration(Exception):
    pass

try:
    i = 1
    while True:
        if i > 20:
            # Stop after printing 20 numbers
            raise StopIteration
        print(i)
        i += 1
except StopIteration:
    print("Stopped after printing 20 numbers")
