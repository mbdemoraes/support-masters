import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-darkgrid')
x = np.arange(100, 1600, 100)
plt.plot(x, [0.0288381116,0.0674303835,0.0870969107,0.1052876151,0.1207936956,0.137807878,0.153561511,0.16498317510000002,0.17423971489999995,0.18404630589999998,0.1925448347,0.2001213311,0.2061662664,0.2120359297,0.2184770417], marker='o', color='#996600', markerfacecolor='None',markeredgecolor='#996600', markeredgewidth=0.8)
plt.plot(x, [0.048761503299999995,0.35017626129999996,0.38336082390000004,0.4087420713,0.4269857191,0.4445793893,0.46063562109999995,0.47414483260000007,0.4874025236,0.5007692828,0.5135183718999999,0.5262958843,0.5382823063,0.5499993834,0.5616207768999999], marker='o', color='#0bf933', markerfacecolor='None',markeredgecolor='#0bf933', markeredgewidth=0.8)
plt.plot(x, [0.0446017505,0.3253509907,0.3573292805,0.3874160453,0.40797441269999996,0.4243838444,0.4396398126,0.45223935280000005,0.46493423199999995,0.477903303,0.49038645779999995,0.5025006033,0.5141117828,0.5250886512999999,0.5365040484], marker='o', color='#7fa1ea', markerfacecolor='None',markeredgecolor='#7fa1ea', markeredgewidth=0.8)
plt.plot(x, [0.0397523437,0.3415445543,0.3767169165,0.40982559690000003,0.43553007879999994,0.4547944188999999,0.4713925029,0.48481369890000003,0.4971766914000001,0.5113126576000001,0.5249044083,0.5380230240999999,0.5518434815,0.5649650235999999,0.5781187012], marker='o', color='#ff0000', markerfacecolor='None',markeredgecolor='#ff0000', markeredgewidth=0.8)
plt.plot(x, [0.044169096,0.3247472498,0.3577502248,0.38499331299999995,0.40344530570000003,0.4210951178999999,0.438007672,0.44991459070000006,0.46267904029999996,0.4760861914,0.4890893417,0.5014457136999999,0.5131307826,0.523998017,0.5352183272000001], marker='o', color='#000000', markerfacecolor='None',markeredgecolor='#000000', markeredgewidth=0.8)
plt.plot(x, [0.036987913299999994,0.3140550338,0.3477661753,0.3757178269,0.39592855200000004,0.4125535001,0.42745027609999997,0.4399952237,0.45192981680000005,0.46462852649999997,0.47679972460000003,0.48857443540000006,0.49960796949999997,0.5101712853,0.5209292781], marker='o', color='#ffcc66', markerfacecolor='None',markeredgecolor='#ffcc66', markeredgewidth=0.8)
plt.legend(['NB', 'Chi-Squared', 'FCBF', 'EFS', 'IG', 'OFS'], fontsize='small', shadow=True, fancybox=True)
plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Time (s)', fontsize=12)
np.arange(100, 1700, step=200)
plt.tight_layout()
plt.savefig('time_usenet1_1000.eps')