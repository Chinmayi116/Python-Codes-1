# Triangle Check Program

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check for valid triangle
if a + b > c and a + c > b and b + c > a:
    print("It is a valid triangle")

    # Check type of triangle
    if a == b == c:
        print("Triangle is Equilateral")
    elif a == b or b == c or a == c:
        print("Triangle is Isosceles")
    else:
        print("Triangle is Scalene")
else:
    print("Not a valid triangle")
