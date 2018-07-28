import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(500)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.gca().set_color_cycle(['blue'])

plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [0.0000000000576233521259079,0.000000000106632434989636,0.000000000154934851555154,	0.00000000020363765339988,0.000000000254430736756573,0.000000000305061052469537,0.000000000355956283975393,0.000000000406557621425018,0.000000000457270357916132,	0.000000000508467081629981], marker="o", color='#ee0fc3')
plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [0.000000000553163713626977,0.00000000105171282521201,0.00000000152761930178975,	0.000000002,0.00000000252635787296481,0.000000003,0.00000000352454974489825,0.000000004,0.00000000449675790575188,0.000000005],  marker="o", color='#ba2323')



#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['NaiveBayes', 'OFS-4'], loc='‘lower right', fontsize='small')


plt.xlabel('Tuplas processadas', fontsize=12)
plt.ylabel('Custo do modelo (RAM-Horas)', fontsize=12)

#plt.show()
plt.tight_layout()
plt.savefig('saved_charts/ram_gradual_drift.png')