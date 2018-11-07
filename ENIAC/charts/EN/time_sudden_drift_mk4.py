import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(500)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.gca().set_color_cycle(['blue'])

plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [73.17,364.63,895.26,1661.07,2658.57,4006.32,5534.29,7407.80,9455.60,11763.26], marker="o", color='#e5914b')


#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['MK-4'], loc='‘lower right', fontsize='small')


plt.xlabel('Tuplas processadas', fontsize=12)
plt.ylabel('Tempo de processamento (em segundos)', fontsize=12)

#plt.show()
plt.tight_layout()
plt.savefig('saved_charts/time_sudden_drift_mk4.png')
