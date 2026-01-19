# Cube Number Series

n = int(input("Enter a value for n: "))

sum_cubes = 0

print("Cube numbers up to", n, "are:")

for i in range(1, n + 1):
    cube = i ** 3
    print(cube, end=" ")
    sum_cubes += cube

print("\nSum of cubes up to", n, "is:", sum_cubes)
