import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(500)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.gca().set_color_cycle(['blue'])


plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [82.38,343.31,817.51,1519.70,2452.86,3749.19,5299.28,7006.65,8910.72,10945.11],  marker="o", color='#e5914b')

#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['MK-4'], loc='‘lower right', fontsize='small')


plt.xlabel('Tuplas processadas', fontsize=12)
plt.ylabel('Tempo de de processamento (em segundos)', fontsize=12)

#plt.show()
plt.savefig('saved_charts/time_gradual_drift_mk4.png')
