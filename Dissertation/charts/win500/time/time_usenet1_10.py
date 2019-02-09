import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-darkgrid')
x = np.arange(100, 1600, 100)
plt.plot(x, [0.0288381116,0.0674303835,0.0870969107,0.1052876151,0.1207936956,0.137807878,0.153561511,0.16498317510000002,0.17423971489999995,0.18404630589999998,0.1925448347,0.2001213311,0.2061662664,0.2120359297,0.2184770417], marker='o', color='#996600', markerfacecolor='None',markeredgecolor='#996600', markeredgewidth=0.8)
plt.plot(x, [0.0472322078,0.0942907731,0.1165424174,0.13930072140000002,0.15974453070000003,0.42153628360000006,0.44016567859999994,0.45434949379999995,0.4670265627,0.47867397599999995,0.49467203070000004,0.5064460991999999,0.5180341705,0.5290098446,0.5396649009], marker='o', color='#0bf933', markerfacecolor='None',markeredgecolor='#0bf933', markeredgewidth=0.8)
plt.plot(x, [0.0466406453,0.0907323084,0.11146482360000001,0.1323728744,0.1520411395,0.3985710228,0.41924051370000004,0.43504494920000003,0.44826487190000003,0.4606223797999999,0.4754616619000001,0.4866050734,0.4970095454,0.5070660311,0.5171106616000001], marker='o', color='#7fa1ea', markerfacecolor='None',markeredgecolor='#7fa1ea', markeredgewidth=0.8)
plt.plot(x, [0.0414631881,0.09022382420000001,0.11509962809999999,0.1378088416,0.1562603669,0.4342582416,0.4514783445000001,0.464358766,0.47730019849999994,0.48958617530000004,0.5064281981,0.5188175723999999,0.5313865471000001,0.5434031871999999,0.5557595323], marker='o', color='#ff0000', markerfacecolor='None',markeredgecolor='#ff0000', markeredgewidth=0.8)
plt.plot(x, [0.0431851165,0.0876533522,0.109576202,0.13013803969999999,0.1482235626,0.3897469673,0.4082424176,0.42166191559999994,0.4331338401,0.4452056057999999,0.46082775349999994,0.4731289578,0.4840631204,0.494086875,0.5038709628], marker='o', color='#000000', markerfacecolor='None',markeredgecolor='#000000', markeredgewidth=0.8)
plt.plot(x, [0.041869774600000007,0.08625032089999998,0.10587864379999998,0.12259388330000001,0.14066654230000003,0.38311057440000007,0.4045852825,0.4203167888,0.4314926563,0.4430905538,0.4577093595000001,0.47021367629999994,0.4820677843,0.4934595625,0.5044360774], marker='o', color='#ffcc66', markerfacecolor='None',markeredgecolor='#ffcc66', markeredgewidth=0.8)
plt.legend(['NB', 'Chi-Squared', 'FCBF', 'EFS', 'IG', 'OFS'], fontsize='small', shadow=True, fancybox=True)
plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Time (s)', fontsize=12)
np.arange(100, 1700, step=200)
plt.tight_layout()
plt.savefig('time_usenet1_10.eps')