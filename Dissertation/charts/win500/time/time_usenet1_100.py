import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-darkgrid')
x = np.arange(100, 1600, 100)
plt.plot(x, [0.0288381116,0.0674303835,0.0870969107,0.1052876151,0.1207936956,0.137807878,0.153561511,0.16498317510000002,0.17423971489999995,0.18404630589999998,0.1925448347,0.2001213311,0.2061662664,0.2120359297,0.2184770417], marker='o', color='#996600', markerfacecolor='None',markeredgecolor='#996600', markeredgewidth=0.8)
plt.plot(x, [0.048844544000000004,0.09723859800000001,0.11962663220000003,0.1402224232,0.16100960860000002,0.42305139789999996,0.44947120179999994,0.4687815934,0.4823209636,0.4956882262000001,0.5158642308,0.5291080032,0.5412778997,0.5526249781000001,0.564049345], marker='o', color='#0bf933', markerfacecolor='None',markeredgecolor='#0bf933', markeredgewidth=0.8)
plt.plot(x, [0.046353236299999996,0.09198515750000001,0.1147868241,0.13702128289999999,0.1577164678,0.41294549300000005,0.43244231400000005,0.4484343035,0.46193888850000003,0.4756466099999999,0.49603950550000003,0.5095213853,0.5221189197,0.5340210471,0.545995643], marker='o', color='#7fa1ea', markerfacecolor='None',markeredgecolor='#7fa1ea', markeredgewidth=0.8)
plt.plot(x, [0.0379933585,0.0868364313,0.10710242870000002,0.12442706480000001,0.1423657048,0.4162989992,0.43574236289999996,0.4498418699,0.4632610509000001,0.47649609030000006,0.5005572896999999,0.5131330724000001,0.5242823011000001,0.5347935173,0.5461670691000001], marker='o', color='#ff0000', markerfacecolor='None',markeredgecolor='#ff0000', markeredgewidth=0.8)
plt.plot(x, [0.046431202500000004,0.0953204356,0.11910455770000002,0.13948520179999999,0.15873202109999998,0.41493713039999996,0.4371904042,0.45485004409999996,0.4692495321,0.4822098885,0.5006910471,0.5130230752999999,0.5248844236,0.5361956851,0.5474972575000001], marker='o', color='#000000', markerfacecolor='None',markeredgecolor='#000000', markeredgewidth=0.8)
plt.plot(x, [0.037466082,0.0785880843,0.0973280786,0.11405554539999999,0.13062475310000002,0.38524361409999996,0.4071314262,0.4217593675,0.4355561079,0.44897434589999996,0.46720697170000003,0.47951223660000003,0.4892552664,0.4988131658,0.5085693193999999], marker='o', color='#ffcc66', markerfacecolor='None',markeredgecolor='#ffcc66', markeredgewidth=0.8)
plt.legend(['NB', 'Chi-Squared', 'FCBF', 'EFS', 'IG', 'OFS'], fontsize='small', shadow=True, fancybox=True)
plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Time (s)', fontsize=12)
np.arange(100, 1700, step=200)
plt.tight_layout()
plt.savefig('time_usenet1_100.eps')