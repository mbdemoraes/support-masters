import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(500)


plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [0.05,0.10,0.14,0.18,0.23,0.27,0.31,0.35,0.39,0.43], marker="o",  markersize=6, color='#ee0fc3')
plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [142.31,743.20,1866,3510.70,5594.10,8671.34,12179.85,16147.82,20576.01,25248.78],  marker="^", markersize=6, color='#e5914b')
plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [217.60,438.36,673.99,921.25,1181.84,1455.26,1743.86,2056.42,2374.74,2706.48],  marker="p", markersize=6, color='#000000')
plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [25.91,51.97,78.69,105.69,132.73,160.10,187.61,215.27,243.11,271.30],  marker="s", markersize=6, color='#e7ade3')
plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [2.36,4.72,7.12,9.55,12.04,14.58,17.19,19.88,22.59,25.39],  marker="d", markersize=6, color='#ba2323')



#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['NaiveBayes', 'Janela-1', 'Janela-10', 'Janela-100',  'Janela-1000'], loc='upper left')


plt.grid(color='k', linestyle=':', linewidth=0.5)

plt.xticks(np.arange(10000, 110000, step=10000))
plt.yticks(np.arange(0, 30000, step=5000))
plt.xticks(rotation=30)

plt.xlabel('Tuplas processadas', fontsize=12)
plt.ylabel('Tempo de de processamento (em segundos)', fontsize=12)
plt.tight_layout()

#plt.show()
plt.savefig('time_incremental_drift_mk.png')
