# Program to add two Date objects using operator overloading

class Date:
    def __init__(self, d, m, y):
        # Initialize day, month, year
        self.day = d
        self.month = m
        self.year = y

    def __add__(self, other):
        # Add two Date objects
        return Date(self.day + other.day,
                    self.month + other.month,
                    self.year + other.year)

    def show(self):
        # Display date in DD-MM-YY format
        print(f"{self.day}-{self.month}-{self.year}")

# Create Date objects
d1 = Date(1, 2, 2024)
d2 = Date(3, 4, 1)

# Add two dates
d3 = d1 + d2

# Display result
d3.show()
