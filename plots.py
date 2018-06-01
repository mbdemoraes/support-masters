import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(1000)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.gca().set_color_cycle(['blue'])

plt.plot([1000,2000,3000,4000,5000,6000,7000,8000,9000], [26.10,54.25,82.57,110.95,139.51,168.28,196.76,225.09,253.51], 'b--')
#plt.plot(x, 2 * x)
#plt.plot(x, 3 * x)
#plt.plot(x, 4 * x)

#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['NB'], loc='upper left')

plt.show()