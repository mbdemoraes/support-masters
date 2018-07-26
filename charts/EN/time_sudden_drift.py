import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(500)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.gca().set_color_cycle(['blue'])


plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [0.04,0.07,0.11,0.14,0.18,0.22,0.26,0.30,0.34,0.38], marker="o", color='#ee0fc3')
plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [0.43,0.81,1.17,1.55,1.91,2.28,2.66,3.02,3.38,3.75],  marker="o", color='#ba2323')

#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['NB', 'OFS-4'], loc='‘lower right', fontsize='small')


plt.xlabel('Tuplas processadas', fontsize=12)
plt.ylabel('Tempo de de processamento (em segundos)', fontsize=12)

#plt.show()
plt.savefig('saved_charts/time_sudden_drift.png')
