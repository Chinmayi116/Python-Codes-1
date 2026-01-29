# Program to compare two Time objects using > operator

class Time:
    def __init__(self, h, m):
        # Initialize hour and minute
        self.hour = h
        self.minute = m

    def __gt__(self, other):
        # Compare two Time objects
        return (self.hour, self.minute) > (other.hour, other.minute)

# Create Time objects
t1 = Time(10, 30)
t2 = Time(9, 45)

# Compare times
if t1 > t2:
    print("Time 1 is greater than Time 2")
else:
    print("Time 2 is greater than Time 1")
