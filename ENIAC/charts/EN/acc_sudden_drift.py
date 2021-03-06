import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(500)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.gca().set_color_cycle(['blue'])

plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [87.96,88.11,88.22,88.33,88.30,81.90,78.63,76.67,75.43,74.38], marker="o", color='#ee0fc3')
plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [87.96,88.11,88.22,88.33,88.30,84.29,80.01,78.75,78.23,77.89],  marker="^", color='#e5914b')
plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [88.01,88.14,88.23,88.34,88.29,83.17,81.08,79.80,78.92,78.10],  marker="v", color='#ba2323')


#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['NaiveBayes', 'IG-4', 'OFS-4'], loc='‘lower right', fontsize='small')


plt.axvline(x=50000, ymax=1, color='#00b0e7', label='drift')

plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Accuracy (%)', fontsize=12)

#plt.grid(color='k', linestyle='-.', linewidth=0.4)
plt.xticks(np.arange(10000, 110000, step=10000))
plt.yticks(np.arange(50, 100, step=5))
plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig('acc_sudden_drift.png')
