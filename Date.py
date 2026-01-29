# Program to compare two Date objects using > operator

class Date:
    def __init__(self, d, m, y):
        # Initialize day, month, year
        self.day = d
        self.month = m
        self.year = y

    def __gt__(self, other):
        # Compare two dates
        return (self.year, self.month, self.day) > (other.year, other.month, other.day)

# Create Date objects
d1 = Date(12, 5, 2024)
d2 = Date(10, 6, 2023)

# Compare dates
if d1 > d2:
    print("Date 1 is later than Date 2")
else:
    print("Date 1 is earlier than Date 2")
