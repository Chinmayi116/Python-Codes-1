# Number Classification Program

num = int(input("Enter a number: "))

if num == 0:
    print("Zero")
elif num > 0:
    if num < 10:
        print("Small positive")                
    else:
        print("Large positive")
else:
    if num > -10:
        print("Small negative")
    else:
        print("Large negative")
