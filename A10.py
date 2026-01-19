# Toll Charges Calculation

vehicle = input("Enter vehicle type (car/bus/truck): ")
return_journey = input("Is it a return journey on the same day? (yes/no): ")

toll = 0

if vehicle.lower() == "car":
    toll = 100
elif vehicle.lower() == "bus":
    toll = 200
elif vehicle.lower() == "truck":
    toll = 300
else:
    print("Invalid vehicle type")

if return_journey.lower() == "yes":
    toll = toll - (toll * 0.25)

print("Final Toll Amount = Rs.", toll)
