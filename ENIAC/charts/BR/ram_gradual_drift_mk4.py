import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(500)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.gca().set_color_cycle(['blue'])

plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [0.0000000941160106105904,0.000000392209462568055,0.000000933944757147898,	0.000001736146222675,0.00000280220472743676,0.00000428316333254659,0.000006054,0.00000800455785980575,0.0000101798078114541,0.000012503947140658], marker="o", color='#e5914b')


#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['MK-4'], loc='‘lower right', fontsize='small')


plt.xlabel('Tuplas processadas', fontsize=12)
plt.ylabel('Custo do modelo (RAM-Horas)', fontsize=12)

#plt.show()
plt.tight_layout()
plt.savefig('saved_charts/ram_gradual_drift_mk4.png')
