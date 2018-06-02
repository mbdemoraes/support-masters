import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(1000)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.gca().set_color_cycle(['blue'])

plt.plot([1000,2000,3000,4000,5000,6000,7000,8000,9000], [26.10,54.25,82.57,110.95,139.51,168.28,196.76,225.09,253.51], 'b--')
plt.plot([1000,2000,3000,4000,5000,6000,7000,8000,9000], [84.98,171.07,257.46,344.62,431.41,518.09,605.33,693.18,780.74], 'r--')
#plt.plot(x, 3 * x)
#plt.plot(x, 4 * x)

#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['NB', 'MK-10'], loc='upper left')

plt.xlabel('Tuplas processadas', fontsize=12)
plt.ylabel('Tempo de de processamento (em segundos)', fontsize=12)

plt.show()
