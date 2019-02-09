import matplotlib.pyplot as plt
import numpy as np

x = np.arange(100, 1600, 100)

plt.gca().set_color_cycle(['blue'])

plt.plot(x, [56.999999999999986,67.0,77.0,71.5,71.39999999999999,71.66666666666666,69.85714285714288,69.625,68.44444444444444,68.5,69.36363636363636,69.91666666666666,70.38461538461537,71.21428571428574,72.13333333333334
], marker="o", color='#996600', markerfacecolor="None",
         markeredgecolor='#996600', markeredgewidth=0.8)
plt.plot(x, [56.999999999999986,59.5,71.33333333333336,67.25,66.79999999999998,66.33333333333334,66.0,65.875,65.1111111111111,65.0,65.0,64.75,65.0,65.28571428571426,65.66666666666664
], marker="o", color='#0bf933', markerfacecolor="None",
         markeredgecolor='#0bf933', markeredgewidth=0.8)
plt.plot(x, [56.999999999999986,67.0,76.33333333333334,71.0,69.79999999999998,69.0,68.42857142857143,68.0,67.1111111111111,66.79999999999998,66.63636363636364,66.25,66.46153846153847,66.64285714285714,67.0
], marker="o", color='#7fa1ea', markerfacecolor="None",
         markeredgecolor='#7fa1ea', markeredgewidth=0.8)
plt.plot(x, [56.999999999999986,61.5,63.33333333333333,64.75,65.60000000000001,65.83333333333334,66.0,66.0,66.0,66.5,66.54545454545453,66.5,66.76923076923076,66.92857142857143,66.93333333333335
], marker="o", color='#ff0000', markerfacecolor="None",
         markeredgecolor='#ff0000', markeredgewidth=0.8)
plt.plot(x, [56.999999999999986,62.0,73.0,68.5,67.8,67.33333333333334,67.0,66.75,65.8888888888889,65.70000000000002,65.63636363636364,65.5,65.76923076923076,66.0,66.39999999999999
], marker="o", color='#000000', markerfacecolor="None",
         markeredgecolor='#000000', markeredgewidth=0.8)
plt.plot(x, [56.999999999999986,66.5,76.0,70.75,69.79999999999998,69.16666666666666,67.57142857142857,66.5,65.66666666666664,65.29999999999998,64.90909090909089,64.91666666666666,65.46153846153845,66.14285714285714,67.39999999999999
], marker="o", color='#ffcc66', markerfacecolor="None",
         markeredgecolor='#ffcc66', markeredgewidth=0.8)


#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper le0t')
plt.legend(['NB', 'Chi-Squared', 'FCBF', 'EFS', 'IG', 'OFS'], loc='‘lower right', fontsize='small', shadow=True, fancybox=True)

plt.axvline(x=300, ymax=1, color='#a1a1ee', ls='--', linewidth=0.8)
plt.axvline(x=600, ymax=1, color='#a1a1ee', ls='--', linewidth=0.8)
plt.axvline(x=900, ymax=1, color='#a1a1ee', ls='--', linewidth=0.8)
plt.axvline(x=1200, ymax=1, color='#a1a1ee', ls='--', linewidth=0.8)



plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Accuracy (%)', fontsize=12)

#plt.grid(color='k', linestyle='-.', linewidth=0.4)
plt.xticks(np.arange(100, 1700, step=200))
plt.yticks(np.arange(20, 120, step=20))

plt.tight_layout()

#plt.show()
plt.savefig('acc_usenet2_10.eps')
