import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(500)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.gca().set_color_cycle(['blue'])


plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [0.000000163672381415053,0.000000850143247463274,0.0000021339227518905,0.00000401180490650125,	0.0000063919176708381,0.00000990742513024243,0.0000139156353884636,0.000018448730338625,0.0000235075878235187,0.0000288458641473349],  marker="o", color='#e5914b')



#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['MK-4'], loc='‘lower right', fontsize='small')


plt.xlabel('Tuplas processadas', fontsize=12)
plt.ylabel('Custo do modelo (RAM-Horas)', fontsize=12)

#plt.show()
plt.tight_layout()
plt.savefig('saved_charts/ram_incremental_drift_mk4.png')
