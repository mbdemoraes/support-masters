import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(500)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.gca().set_color_cycle(['blue'])

plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [80.64,84.65,87.18,88.75,90.12,91.04,91.65,92.15,92.55,92.91], marker="o", color='#ee0fc3')
plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [80.46,84.90,87.67,89.28,90.38,91.12,91.66,92.06,92.40,92.72],  marker="^", color='#e5914b')
plt.plot([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000], [80.71,84.68,87.17,88.73,90.11,91.04,91.64,92.12,92.52,92.87],  marker="v", color='#ba2323')



#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['NaiveBayes', 'IG-4', 'OFS-4'], loc='‘lower right', fontsize='small', shadow=True, fancybox=True)

plt.axvline(x=40000, ymax=1, color='#00b0e7', ls='--', linewidth=2)
plt.axvline(x=60000, ymax=1, color='#00b0e7', ls='--', linewidth=2)
plt.axvline(x=50000, ymax=1, color='#00b0e7', label='drift')

plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Accuracy (%)', fontsize=12)

#plt.grid(color='k', linestyle='-.', linewidth=0.4)
plt.xticks(np.arange(10000, 110000, step=10000))
plt.yticks(np.arange(50, 100, step=5))
plt.xticks(rotation=30)

plt.tight_layout()

#plt.show()
plt.savefig('acc_gradual_drift.png')
