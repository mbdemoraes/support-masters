import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-darkgrid')
x = np.arange(100, 1600, 100)
plt.plot(x, [0.0288381116,0.0674303835,0.0870969107,0.1052876151,0.1207936956,0.137807878,0.153561511,0.16498317510000002,0.17423971489999995,0.18404630589999998,0.1925448347,0.2001213311,0.2061662664,0.2120359297,0.2184770417], marker='o', color='#996600', markerfacecolor='None',markeredgecolor='#996600', markeredgewidth=0.8)
plt.plot(x, [0.043642327799999985,0.0895781395,0.11319372360000002,0.13574308159999998,0.1571885511,0.1753687856,0.19028044610000003,0.2029240804,0.2135042129,0.22294114279999996,0.47851569150000006,0.49336975270000005,0.5053943261,0.5166877294,0.5265072135], marker='o', color='#0bf933', markerfacecolor='None',markeredgecolor='#0bf933', markeredgewidth=0.8)
plt.plot(x, [0.0462284683,0.09142261680000001,0.11110811930000002,0.12996362079999998,0.14683338070000002,0.1643050107,0.1780150803,0.1889966191,0.1984672151,0.2076258683,0.4500569929999999,0.46384669450000005,0.4748021113,0.48504219210000005,0.49448854750000015], marker='o', color='#7fa1ea', markerfacecolor='None',markeredgecolor='#7fa1ea', markeredgewidth=0.8)
plt.plot(x, [0.038853770100000004,0.0847350995,0.1070852087,0.1265153218,0.14164165839999998,0.15795938999999998,0.17201490500000002,0.18466628999999998,0.1962614154,0.2073649006,0.4611090433999999,0.47580970679999995,0.48645536330000005,0.4966586384999999,0.5067912794], marker='o', color='#ff0000', markerfacecolor='None',markeredgecolor='#ff0000', markeredgewidth=0.8)
plt.plot(x, [0.047006443599999996,0.08889443520000001,0.10626515410000001,0.12345041060000002,0.14159846039999996,0.15963575309999997,0.1743903795,0.1848742452,0.19409326529999998,0.20270864589999998,0.4443364517,0.4574990134,0.46756472020000006,0.4771479487,0.4870726641000001], marker='o', color='#000000', markerfacecolor='None',markeredgecolor='#000000', markeredgewidth=0.8)
plt.plot(x, [0.04203782810000001,0.0865701364,0.10536818330000002,0.12357113229999998,0.1427339268,0.1611048483,0.1773067884,0.19037618809999998,0.20050909109999998,0.2097240379,0.4803002633999999,0.4965426408,0.5108928679,0.5241091036,0.5368777284], marker='o', color='#ffcc66', markerfacecolor='None',markeredgecolor='#ffcc66', markeredgewidth=0.8)
plt.legend(['NB', 'Chi-Squared', 'FCBF', 'EFS', 'IG', 'OFS'], fontsize='small', shadow=True, fancybox=True)
plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Time (s)', fontsize=12)
np.arange(100, 1700, step=200)
plt.tight_layout()
plt.savefig('time_usenet1_10.eps')