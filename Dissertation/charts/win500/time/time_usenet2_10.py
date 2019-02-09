import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-darkgrid')
x = np.arange(100, 1600, 100)
plt.plot(x, [0.031253311699999994,0.07215770070000001,0.09163049990000001,0.10744159990000002,0.12148039160000002,0.13709258269999997,0.15257350639999998,0.16390463299999997,0.1728363921,0.18036022219999998,0.1870883563,0.1934477962,0.19908983060000002,0.20466751290000001,0.21117373059999997], marker='o', color='#996600', markerfacecolor='None',markeredgecolor='#996600', markeredgewidth=0.8)
plt.plot(x, [0.0446493979,0.0906154491,0.1104269819,0.1276958955,0.145811462,0.390137078,0.40879729429999995,0.4225411467,0.43427693359999997,0.4449124119,0.45944531780000003,0.47052372889999994,0.48084150580000007,0.4907270469,0.5003461117], marker='o', color='#0bf933', markerfacecolor='None',markeredgecolor='#0bf933', markeredgewidth=0.8)
plt.plot(x, [0.0483705535,0.09613628970000002,0.1170029821,0.13590092999999998,0.1548701036,0.40134515119999997,0.41869511710000007,0.43034649190000007,0.4414845552,0.4530571365999999,0.46766673219999993,0.4799649875,0.4912914289,0.5020920276,0.5133426316999999], marker='o', color='#7fa1ea', markerfacecolor='None',markeredgecolor='#7fa1ea', markeredgewidth=0.8)
plt.plot(x, [0.0369955623,0.07658203899999999,0.09545897249999999,0.11339363890000001,0.12920571539999998,0.37170214980000005,0.3877505193,0.39911431270000003,0.4089831277,0.41807018120000006,0.4309334617,0.44004815510000006,0.4488585079,0.457421832,0.46609738510000004], marker='o', color='#ff0000', markerfacecolor='None',markeredgecolor='#ff0000', markeredgewidth=0.8)
plt.plot(x, [0.0442681984,0.0903272619,0.11262698460000001,0.13451222079999997,0.15486185440000003,0.40966349159999993,0.4266315496,0.439599838,0.45124401320000007,0.4632289963,0.4788349846,0.4911903743,0.502561578,0.5135519575999999,0.5244406352], marker='o', color='#000000', markerfacecolor='None',markeredgecolor='#000000', markeredgewidth=0.8)
plt.plot(x, [0.044300936299999996,0.0880345283,0.1123078954,0.13306089579999997,0.15267704799999998,0.3930201371,0.40935207149999997,0.4221149254,0.43377598289999997,0.44598190130000004,0.4592050005,0.47064004270000004,0.4817750437,0.49235784029999996,0.5027286685], marker='o', color='#ffcc66', markerfacecolor='None',markeredgecolor='#ffcc66', markeredgewidth=0.8)
plt.legend(['NB', 'Chi-Squared', 'FCBF', 'EFS', 'IG', 'OFS'], fontsize='small', shadow=True, fancybox=True)
plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Time (s)', fontsize=12)
np.arange(100, 1700, step=200)
plt.tight_layout()
plt.savefig('time_usenet2_10.eps')