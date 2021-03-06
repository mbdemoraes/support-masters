import matplotlib.pyplot as plt
import numpy as np

x = np.arange(100, 1600, 100)

plt.gca().set_color_cycle(['blue'])

plt.plot(x, [52.0,56.000000000000014,70.0,57.499999999999986,52.8,53.66666666666667,56.000000000000014,60.124999999999986,63.0,59.8,58.63636363636364,58.5,60.07692307692308,61.71428571428571,63.33333333333333
], marker="o", color='#996600', markerfacecolor="None",
         markeredgecolor='#996600', markeredgewidth=0.8)
plt.plot(x, [52.0,48.5,64.0,53.0,48.60000000000001,45.83333333333332,49.0,51.249999999999986,54.22222222222223,51.8,49.9090909090909,48.33333333333333,49.92307692307692,51.28571428571429,52.733333333333334
], marker="o", color='#0bf933', markerfacecolor="None",
         markeredgecolor='#0bf933', markeredgewidth=0.8)
plt.plot(x, [52.0,49.0,64.33333333333334,53.25,49.199999999999996,46.33333333333332,49.42857142857144,51.625,54.55555555555556,51.39999999999999,49.63636363636363,48.08333333333333,47.307692307692314,48.85714285714285,50.39999999999999
], marker="o", color='#7fa1ea', markerfacecolor="None",
         markeredgecolor='#7fa1ea', markeredgewidth=0.8)
plt.plot(x, [52.0,65.0,66.0,59.0,58.2,60.16666666666667,56.857142857142875,55.000000000000014,55.8888888888889,54.7,55.90909090909089,57.08333333333333,55.92307692307692,54.71428571428571,54.06666666666666
], marker="o", color='#ff0000', markerfacecolor="None",
         markeredgecolor='#ff0000', markeredgewidth=0.8)
plt.plot(x, [52.0,50.5,65.66666666666664,54.25,49.60000000000001,46.66666666666667,49.714285714285715,51.875000000000014,54.777777777777786,51.60000000000001,49.81818181818182,48.25,49.846153846153854,51.21428571428571,52.60000000000001
], marker="o", color='#000000', markerfacecolor="None",
         markeredgecolor='#000000', markeredgewidth=0.8)
plt.plot(x, [52.0,66.0,76.0,62.5,55.2,50.66666666666668,53.71428571428571,56.75,59.44444444444444,55.7,52.90909090909089,50.66666666666668,53.0,54.78571428571429,56.533333333333346
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
plt.savefig('acc_usenet1_10.eps')
