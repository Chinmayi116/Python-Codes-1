import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[1:4])      # From index 1 to 3
print(arr[:3])       # First 3 elements
print(arr[2:])       # From index 2 to end
print(arr[::2])      # Every 2nd element
print(arr[-4:-1])    # Negative index slicing
