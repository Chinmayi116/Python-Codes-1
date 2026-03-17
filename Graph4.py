import numpy as np
import matplotlib.pyplot as plt

x = np.arange(5)
y = np.random.randint(10,50,5)

plt.bar(x,y)

plt.title("Random Bar Graph")
plt.xlabel("X values")
plt.ylabel("Random values")

plt.show()
