import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(500)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.gca().set_color_cycle(['blue'])


plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [0.0000000835998977080087,0.000000416569647457888,0.00000102277318112972,	0.00000189764379223535,0.00000303721858981657,0.00000457691695501063,0.00000632250286815705,0.00000846284271668161,0.000010802294535302,0.0000134386122126083],  marker="o", color='#e5914b')



#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['MK-4'], loc='‘lower right', fontsize='small')


plt.xlabel('Tuplas processadas', fontsize=12)
plt.ylabel('Custo do modelo (RAM-Horas)', fontsize=12)

#plt.show()
plt.tight_layout()
plt.savefig('saved_charts/ram_sudden_drift_mk4.png')
