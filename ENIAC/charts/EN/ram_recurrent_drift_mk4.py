import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(500)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.gca().set_color_cycle(['blue'])


plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [0.000000113678394943631,0.000000626920635592804,0.00000146555160167644,	0.0000027054260439779,0.00000442068232824103,0.00000652178178780555,0.0000089623568728961,0.0000118318462561931,0.000015139324146716,0.000018808],  marker="o", color='#e5914b')



#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['MK-4'], loc='‘lower right', fontsize='small')


plt.xlabel('Tuplas processadas', fontsize=12)
plt.ylabel('Custo do modelo (RAM-Horas)', fontsize=12)

#plt.show()
plt.tight_layout()
plt.savefig('saved_charts/ram_recurrent_drift_mk4.png')
