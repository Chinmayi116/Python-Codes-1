import random

user = input("Choose Heads or Tails: ").lower()

result = random.choice(["heads", "tails"])

print("Coin shows:", result)

if user == result:
    print("You won!")
else:
    print("You lost!")
