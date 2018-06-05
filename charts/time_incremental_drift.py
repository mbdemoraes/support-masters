import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(1000)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.gca().set_color_cycle(['blue'])

plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [0.058,0.10,0.14,0.18,0.23,0.27,0.31,0.35,0.39,0.43], 'bo')
plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [142.31,743.20,1866.93,3510.70,5594.10,8671.34,12179.85,16147.82,20576.012,25248.248], 'r--')
plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [0.45,0.83,1.22,1.61,1.99,2.38,2.76,3.14,3.53,3.91], 'g--')
#plt.plot(x, 3 * x)
#plt.plot(x, 4 * x)

#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['NB', 'MK-4', 'OFS-4'], loc='upper left')

plt.xlabel('Tuplas processadas', fontsize=12)
plt.ylabel('Tempo de de processamento (em segundos)', fontsize=12)

plt.show()
