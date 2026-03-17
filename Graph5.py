import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x,y)

plt.title("Scatter Plot using NumPy")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.show()
