import matplotlib.pyplot as plt
import numpy as np

Time = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
Voltage = np.array([6, 3.1, 1.8, 1, 0.6, 0.4, 0.2, 0.1, 0.001, 0.001, 0.001])

logVoltage = np.log(Voltage)
print(logVoltage)
 
curve_fit = np.polyfit(Time, logVoltage, 1)
print(curve_fit)

y = np.array(6*(2.54778e-3)**Time)

plt.plot(Time, Voltage, 'ro')
plt.plot(Time, y, 'b-')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Voltage vs Time')
plt.grid(True)
plt.show()
