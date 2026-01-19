# Water Bill Calculation

litres = int(input("Enter water consumption in litres: "))

bill = 0

if litres <= 10000:
    bill = 100
elif litres <= 20000:
    bill = 100 + ((litres - 10000) / 1000) * 5
else:
    bill = 100 + (10000 / 1000) * 5 + ((litres - 20000) / 1000) * 8

print("Final Water Bill = Rs.", bill)
