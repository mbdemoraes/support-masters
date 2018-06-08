import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(500)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.gca().set_color_cycle(['blue'])


plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [64.30,354.78,829.44,1531.26,2502.18,3691.45,5072.88,6697.08,8569.19,10645.71],  marker="o", color='#e5914b')

#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['MK-4'], loc='‘lower right', fontsize='small')


plt.xlabel('Tuplas processadas', fontsize=12)
plt.ylabel('Tempo de de processamento (em segundos)', fontsize=12)

#plt.show()
plt.savefig('saved_charts/time_recurrent_drift_mk4.png')
