import matplotlib.pyplot as plt
import numpy as np
INTEREST_RATE = 0.048
COMPOUND_NUMBER = 12
YEARS = 5


initial_deposit = int((input("Money in: ")))

money = [initial_deposit]

for i in range(YEARS):
    money.append(money[i] * (1+INTEREST_RATE/COMPOUND_NUMBER) ** COMPOUND_NUMBER)

m = np.array(money)
y = np.arange(0, YEARS + 1, 1)

plt.plot(y, m)
plt.show()




