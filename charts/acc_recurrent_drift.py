import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(500)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.gca().set_color_cycle(['blue'])

plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [87.72,87.93,78.97,78.19,78.56,75.73,75.37,75.96,73.97,73.53], marker="o", color='#ee0fc3')
plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [87.72,87.93,81.09,78.81,79.18,77.63,76.61,75.96,73.83,72.18],  marker="o", color='#e5914b')
plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [71.28,71.04,68.98,69.25,69.46,64.21,64.10,64.85,63.69,63.69],  marker="o", color='#ba2323')



#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['NaiveBayes', 'MK-4', 'OFS-4'], loc='‘lower right', fontsize='small')

plt.axvline(x=30000, ymax=1, color='#00b0e7', ls='--')
plt.axvline(x=60000, ymax=1, color='#00b0e7', ls='--')


plt.xlabel('Tuplas processadas', fontsize=12)
plt.ylabel('Acurácia (%)', fontsize=12)

#plt.show()
plt.savefig('saved_charts/acc_recurrent_drift.png')
