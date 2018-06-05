import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(500)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.gca().set_color_cycle(['blue'])

plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [80.09,80.26,79.21,80.14,80.14,79.27,78.77,78.27,77.89,77.60], marker="o", color='#ee0fc3')
plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [77.05,75.59,72.48,73.56,74.3,73.79,73.63,72.98,72.09,71.65],  marker="o", color='#e5914b')
plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [76.87,75.24,74.91,76.80,77.84,77.55,77.48,77.24,77.10,76.93],  marker="o", color='#ba2323')



#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['NaiveBayes', 'MK-4', 'MK-10', 'MK-100',  'OFS-4','OFS-10', 'OFS-100'], loc='‘lower right', fontsize='small')

plt.xlabel('Tuplas processadas', fontsize=12)
plt.ylabel('Acurácia (%)', fontsize=12)

#plt.show()
plt.savefig('saved_charts/acc_incremental_drift.png')
