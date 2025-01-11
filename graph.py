import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.set_title('Stock Market Graph')
ax.set_xlabel('Date')
ax.set_ylabel('Stock Price')
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.show()