import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-darkgrid')
x = np.arange(100, 1600, 100)
plt.plot(x, [5.282581611099755e-10,1.221505797105738e-09,1.5516517253826476e-09,1.8207635639883164e-09,2.0597680495544855e-09,2.3256882381490945e-09,2.5898211198575377e-09,2.783338478423862e-09,2.9359154821185184e-09,3.064488216679129e-09,3.179477438184536e-09,3.288218025497265e-09,3.3847616977211504e-09,3.4802388397887767e-09,3.591623845862225e-09], marker='o', color='#996600', markerfacecolor='None',markeredgecolor='#996600', markeredgewidth=0.8)
plt.plot(x, [7.866745676975698e-10,5.897440596686676e-09,6.434902429056044e-09,6.91908967254497e-09,7.269560012998887e-09,7.564500458749012e-09,7.858412322991631e-09,8.10603563343837e-09,8.351125233265469e-09,8.590444740363088e-09,8.824113034080092e-09,9.048962875860226e-09,9.258850174967406e-09,9.46073282345964e-09,9.661747358598642e-09], marker='o', color='#0bf933', markerfacecolor='None',markeredgecolor='#0bf933', markeredgewidth=0.8)
plt.plot(x, [7.648258992623951e-10,5.879200218432065e-09,6.504565418241339e-09,7.0286312781924175e-09,7.400106190014216e-09,7.691856036668848e-09,7.967393774348e-09,8.1956664701278e-09,8.45007913726444e-09,8.703777304102149e-09,8.949630246475753e-09,9.181790187187492e-09,9.399846824236214e-09,9.607561558950692e-09,9.814956006422225e-09], marker='o', color='#7fa1ea', markerfacecolor='None',markeredgecolor='#7fa1ea', markeredgewidth=0.8)
plt.plot(x, [6.50155865304172e-10,5.691992217052727e-09,6.238893343502034e-09,6.694461367555377e-09,7.0233723698159055e-09,7.316160575438289e-09,7.583729561799516e-09,7.82505439155673e-09,8.045394831719498e-09,8.27862188995609e-09,8.520602023664654e-09,8.753417610696828e-09,8.969493704277817e-09,9.184385223024213e-09,9.40810139725171e-09], marker='o', color='#ff0000', markerfacecolor='None',markeredgecolor='#ff0000', markeredgewidth=0.8)
plt.plot(x, [7.872175984196367e-10,5.925708504637703e-09,6.5924100504970805e-09,7.054925624183276e-09,7.3991983828083084e-09,7.682388827047208e-09,7.964179383496238e-09,8.186623891005706e-09,8.44942278137824e-09,8.702678023807913e-09,8.947586857280592e-09,9.171199398978095e-09,9.388594709909834e-09,9.590471138524514e-09,9.798846022206876e-09], marker='o', color='#000000', markerfacecolor='None',markeredgecolor='#000000', markeredgewidth=0.8)
plt.plot(x, [6.410332405720319e-10,5.5142500603985455e-09,6.106511033064789e-09,6.5775262474069995e-09,6.89247746368332e-09,7.1549691060086105e-09,7.4052811070084576e-09,7.630039983332156e-09,7.854579870263735e-09,8.087189806172831e-09,8.307052016681266e-09,8.511029634319244e-09,8.712569757411048e-09,8.905616694536061e-09,9.10261365431009e-09], marker='o', color='#ffcc66', markerfacecolor='None',markeredgecolor='#ffcc66', markeredgewidth=0.8)
plt.legend(['NB', 'Chi-Squared', 'FCBF', 'EFS', 'IG', 'OFS'], fontsize='small', shadow=True, fancybox=True)
plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Memory Consumption (RAM-hours)', fontsize=12)
np.arange(100, 1700, step=200)
plt.tight_layout()
plt.savefig('memory_usenet2_1000.eps')