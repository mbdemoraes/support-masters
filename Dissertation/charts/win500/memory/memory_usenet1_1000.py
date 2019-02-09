import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-darkgrid')
x = np.arange(100, 1600, 100)
plt.plot(x, [4.876740481365059e-10,1.1417359206260492e-09,1.475207056068505e-09,1.7849713928697423e-09,2.049308855301804e-09,2.33953151033322e-09,2.6083499154485765e-09,2.80324804003516e-09,2.9612007018702313e-09,3.1285799734755938e-09,3.2736331892425403e-09,3.4029648009751817e-09,3.506152499337784e-09,3.6063604336215386e-09,3.7163242415984477e-09], marker='o', color='#996600', markerfacecolor='None',markeredgecolor='#996600', markeredgewidth=0.8)
plt.plot(x, [8.308815533736099e-10,1.5710588827569865e-09,1.965959986152334e-09,2.32193264770632e-09,2.6473064316529782e-09,7.375216098559606e-09,7.768305850499827e-09,8.037776364170429e-09,8.26684174615745e-09,8.501806805238748e-09,8.843655267816865e-09,9.069431803921444e-09,9.287341192972744e-09,9.495898536283108e-09,9.700479300033509e-09], marker='o', color='#0bf933', markerfacecolor='None',markeredgecolor='#0bf933', markeredgewidth=0.8)
plt.plot(x, [7.993238004741982e-10,1.5426112914633835e-09,1.90857405171502e-09,2.2483031233677435e-09,2.537837050427165e-09,7.087113840757145e-09,7.484479380937914e-09,7.771995507686088e-09,8.029023291749465e-09,8.281351212460962e-09,8.647697466327704e-09,8.872853997744413e-09,9.081322095842619e-09,9.27542430426139e-09,9.4707999039015e-09], marker='o', color='#7fa1ea', markerfacecolor='None',markeredgecolor='#7fa1ea', markeredgewidth=0.8)
plt.plot(x, [6.32244220101792e-10,1.360783240084019e-09,1.73952206703441e-09,2.079014846522775e-09,2.3755528804500484e-09,7.198308706479976e-09,7.620955419780065e-09,7.945329403547985e-09,8.233984999970016e-09,8.482989972452529e-09,8.955144226263795e-09,9.221396905550527e-09,9.454027218854264e-09,9.679109243791759e-09,9.898208775921001e-09], marker='o', color='#ff0000', markerfacecolor='None',markeredgecolor='#ff0000', markeredgewidth=0.8)
plt.plot(x, [8.152120167495062e-10,1.633542406629978e-09,2.0240172241270123e-09,2.382943143520711e-09,2.6868528591110886e-09,7.249662110926583e-09,7.688415065881072e-09,7.966885097742701e-09,8.207079979397769e-09,8.454365095097572e-09,8.828174977060201e-09,9.073681675094077e-09,9.299830443331143e-09,9.509400993863534e-09,9.716577236984338e-09], marker='o', color='#000000', markerfacecolor='None',markeredgecolor='#000000', markeredgewidth=0.8)
plt.plot(x, [6.271496643790354e-10,1.415996548620984e-09,1.8016109502868106e-09,2.1235818060932473e-09,2.424735513649053e-09,7.063310928562449e-09,7.470793427998199e-09,7.739361526140322e-09,7.93675074617606e-09,8.145950999418687e-09,8.463550063679202e-09,8.676246801880913e-09,8.87762512330504e-09,9.059796615325328e-09,9.262665929948705e-09], marker='o', color='#ffcc66', markerfacecolor='None',markeredgecolor='#ffcc66', markeredgewidth=0.8)
plt.legend(['NB', 'Chi-Squared', 'FCBF', 'EFS', 'IG', 'OFS'], fontsize='small', shadow=True, fancybox=True)
plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Memory Consumption (RAM-hours)', fontsize=12)
np.arange(100, 1700, step=200)
plt.tight_layout()
plt.savefig('memory_usenet1_1000.eps')