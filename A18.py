# Traffic Signal Logic

signal = input("Enter traffic signal color (Red/Yellow/Green): ").lower()

if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Ready")
elif signal == "green":
    print("Go")
else:
    print("Invalid signal")
