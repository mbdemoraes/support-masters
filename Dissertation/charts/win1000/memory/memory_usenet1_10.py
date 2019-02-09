import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-darkgrid')
x = np.arange(100, 1600, 100)
plt.plot(x, [4.876740481365059e-10,1.1417359206260492e-09,1.475207056068505e-09,1.7849713928697423e-09,2.049308855301804e-09,2.33953151033322e-09,2.6083499154485765e-09,2.80324804003516e-09,2.9612007018702313e-09,3.1285799734755938e-09,3.2736331892425403e-09,3.4029648009751817e-09,3.506152499337784e-09,3.6063604336215386e-09,3.7163242415984477e-09], marker='o', color='#996600', markerfacecolor='None',markeredgecolor='#996600', markeredgewidth=0.8)
plt.plot(x, [7.380244228032729e-10,1.5165446170193867e-09,1.9169770657113854e-09,2.3009636762663724e-09,2.6665519361940936e-09,2.9766647468857045e-09,3.2311158181548945e-09,3.446865519026295e-09,3.6274038332398568e-09,3.788473715001304e-09,8.180250480917593e-09,8.435532464491825e-09,8.64218685401231e-09,8.83629872276489e-09,9.005076757003451e-09], marker='o', color='#0bf933', markerfacecolor='None',markeredgecolor='#0bf933', markeredgewidth=0.8)
plt.plot(x, [7.817579939946947e-10,1.5477084793684382e-09,1.8815013653046146e-09,2.202586343036551e-09,2.4901709150245622e-09,2.788196569570651e-09,3.0221438148754343e-09,3.2095316857194736e-09,3.371136980968631e-09,3.527457225333072e-09,7.693378230410112e-09,7.930368121889524e-09,8.118647979763442e-09,8.294655261843363e-09,8.457019931809148e-09], marker='o', color='#7fa1ea', markerfacecolor='None',markeredgecolor='#7fa1ea', markeredgewidth=0.8)
plt.plot(x, [6.570463285824905e-10,1.4346431567099776e-09,1.8136178590756738e-09,2.144487734482727e-09,2.402351572654935e-09,2.680694385592101e-09,2.920536276372149e-09,3.1364182344068676e-09,3.3342762851270116e-09,3.5237909967181165e-09,7.884114184237395e-09,8.136759872314209e-09,8.319716187841568e-09,8.495090852489279e-09,8.669251449454575e-09], marker='o', color='#ff0000', markerfacecolor='None',markeredgecolor='#ff0000', markeredgewidth=0.8)
plt.plot(x, [7.949141385149624e-10,1.5048318726072711e-09,1.79937464043436e-09,2.0920174906189658e-09,2.4013935081253033e-09,2.709068061853655e-09,2.9608395190737726e-09,3.1397351463184592e-09,3.2970475757757407e-09,3.4440952225503404e-09,7.596212046817566e-09,7.822423909987635e-09,7.995413206543153e-09,8.160130461687843e-09,8.330717219457446e-09], marker='o', color='#000000', markerfacecolor='None',markeredgecolor='#000000', markeredgewidth=0.8)
plt.plot(x, [7.108911321500524e-10,1.4656247489853865e-09,1.7843696895686702e-09,2.0943425361843157e-09,2.421017253965967e-09,2.7343827444584005e-09,3.0108510167265512e-09,3.233865935454766e-09,3.4067727705732816e-09,3.5640538362633022e-09,8.213618460771731e-09,8.49276005476444e-09,8.739383142518296e-09,8.966544799766607e-09,9.186012887063955e-09], marker='o', color='#ffcc66', markerfacecolor='None',markeredgecolor='#ffcc66', markeredgewidth=0.8)
plt.legend(['NB', 'Chi-Squared', 'FCBF', 'EFS', 'IG', 'OFS'], fontsize='small', shadow=True, fancybox=True)
plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Memory Consumption (RAM-hours)', fontsize=12)
np.arange(100, 1700, step=200)
plt.tight_layout()
plt.savefig('memory_usenet1_10.eps')