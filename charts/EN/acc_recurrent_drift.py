import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(500)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.gca().set_color_cycle(['blue'])

plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [87.72,87.93,78.97,78.19,78.56,75.73,75.37,75.96,73.97,73.53], marker="o", color='#ee0fc3')
plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [87.72,87.93,81.09,78.81,79.18,77.63,76.61,75.96,73.83,72.18],  marker="^", color='#e5914b')
plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [71.28,71.04,68.98,69.25,69.46,64.21,64.10,64.85,63.69,63.69],  marker="v", color='#ba2323')



#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['NaiveBayes', 'IG-4', 'OFS-4'], loc='‘lower right', fontsize='small', shadow=True, fancybox=True)

plt.axvline(x=30000, ymax=1, color='#00b0e7', ls='--', linewidth=2)
plt.axvline(x=60000, ymax=1, color='#00b0e7', ls='--', linewidth=2)


plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Accuracy (%)', fontsize=12)

#plt.grid(color='k', linestyle='-.', linewidth=0.4)
plt.xticks(np.arange(10000, 110000, step=10000))
plt.yticks(np.arange(50, 100, step=5))
plt.xticks(rotation=30)

plt.tight_layout()

#plt.show()
plt.savefig('acc_recurrent_drift.png')
