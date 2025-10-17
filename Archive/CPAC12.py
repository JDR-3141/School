import matplotlib.pyplot as plt
import numpy as np

x_values = np.array([3.66, 3.55, 3.46, 3.41, 3.34, 3.32, 3.30, 3.17, 3.13, 2.92, 2.87, 2.83])
y_values = np.array([3.33, 3.00, 2.71, 2.56, 2.40, 2.20, 2.04, 1.67, 1.39, 0.833, 0.470, 0.182])

c = np.polyfit(x_values, y_values, 1)
poly = np.poly1d(c)

plt.scatter(x_values, y_values, color='black')
plt.plot(x_values, poly(x_values), color='red')
plt.xlabel('1/temperature (o K^3)')
plt.ylabel('ln(Resistance) (kΩ)')
plt.title('CPAC 12')
plt.show()


