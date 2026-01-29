# Program to add and subtract two Distance objects

class Distance:
    def __init__(self, meter):
        # Initialize distance in meters
        self.meter = meter

    def __add__(self, other):
        # Add two distances
        return Distance(self.meter + other.meter)

    def __sub__(self, other):
        # Subtract two distances
        return Distance(self.meter - other.meter)

    def show(self):
        # Display distance
        print("Distance:", self.meter, "meters")

# Create Distance objects
d1 = Distance(100)
d2 = Distance(40)

# Add distances
d3 = d1 + d2

# Subtract distances
d4 = d1 - d2

# Display results
d3.show()
d4.show()
