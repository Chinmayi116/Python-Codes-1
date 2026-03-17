import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)

plt.hist(data)

plt.title("Histogram using NumPy")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()
