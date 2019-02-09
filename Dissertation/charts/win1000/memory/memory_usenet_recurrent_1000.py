import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-darkgrid')
x = np.arange(100, 6100, 100)
plt.plot(x, [1.1196647590246053e-08,2.479919293327671e-08,3.207726468009357e-08,3.6845931794184986e-08,4.081179172141209e-08,4.4772931024823546e-08,4.8671615511800256e-08,5.265061462708687e-08,5.6380100161477294e-08,5.9557530672439894e-08,6.283133324378376e-08,6.705886206478025e-08,7.026742631150182e-08,7.34838030366527e-08,7.666237782168408e-08,7.990128372409587e-08,8.321329006497335e-08,8.642881613810693e-08,8.961625479636258e-08,9.295476344779671e-08,9.619958238701896e-08,9.941917418257003e-08,1.0267049717905455e-07,1.0595737919320394e-07,1.0924237727221909e-07,1.1243789781046223e-07,1.158309652979347e-07,1.1907959848146616e-07,1.2233544724708237e-07,1.2555594778490812e-07,1.289334220084068e-07,1.320920776903257e-07,1.3526959288230167e-07,1.3859247933187356e-07,1.4183970389788866e-07,1.4495343764129985e-07,1.480689709417944e-07,1.5122223729475258e-07,1.54329618322692e-07,1.5748042072548263e-07,1.6061086989350825e-07,1.637421007804045e-07,1.668611918905421e-07,1.6997887641073765e-07,1.7310657379320554e-07,1.762898994859412e-07,1.7941651650917116e-07,1.8255194626595847e-07,1.8577097093136712e-07,1.8889126537430953e-07,1.9218939283847563e-07,1.9556538771688942e-07,1.988165108691036e-07,2.022198695204461e-07,2.0566494102820337e-07,2.0891475587162501e-07,2.1208457063195404e-07,2.1527458832653778e-07,2.184614695163587e-07,2.2031251281998268e-07], marker='o', color='#996600', markerfacecolor='None',markeredgecolor='#996600', markeredgewidth=0.8)
plt.plot(x, [1.565318341352418e-08,2.9244836565069436e-08,3.7035644528864986e-08,4.16402450120596e-08,4.607584067680915e-08,5.051247678127947e-08,5.500509287820363e-08,5.9077214967081314e-08,6.26812874780943e-08,6.616742813996804e-08,1.0470321188741591e-07,1.1172047899489933e-07,1.165050262866575e-07,1.2070472657199204e-07,1.2473560977918902e-07,1.2885317652258942e-07,1.328824487248328e-07,1.3705371085379067e-07,1.4118668693245554e-07,1.4530018518235388e-07,1.5185084686185647e-07,1.5607203557695053e-07,1.6025629149894748e-07,1.6448027182012277e-07,1.6854699574408535e-07,1.7260183081717127e-07,1.76711084548119e-07,1.8077586963003542e-07,1.851446435408149e-07,1.893129789726299e-07,1.9550594590367377e-07,2.0038481759036103e-07,2.0464287787022256e-07,2.0889261281143253e-07,2.1306587939531422e-07,2.1717118909012817e-07,2.2136342304378726e-07,2.2543071742019286e-07,2.2946443589805298e-07,2.3361410772562293e-07,2.396118672233425e-07,2.4387648198736956e-07,2.4812528369298743e-07,2.521628003608551e-07,2.564451090352653e-07,2.6070984180788966e-07,2.6482567748878916e-07,2.687723566730567e-07,2.72789093268172e-07,2.7690706456893414e-07,2.8327645036484676e-07,2.8762977182721963e-07,2.9201964410751063e-07,2.966404603162897e-07,3.011749187057209e-07,3.0556079704668313e-07,3.096394657469624e-07,3.1367526897138027e-07,3.1778406084557726e-07,3.199519243447381e-07], marker='o', color='#0bf933', markerfacecolor='None',markeredgecolor='#0bf933', markeredgewidth=0.8)
plt.plot(x, [1.6396090217180554e-08,3.038345690583438e-08,3.787880566640508e-08,4.286200640066899e-08,4.773628574821787e-08,5.231863079118708e-08,5.7090010011418825e-08,6.215913183313608e-08,6.653947841431076e-08,7.070283942121888e-08,1.165503806075135e-07,1.2477842252401966e-07,1.2933488003927925e-07,1.3369984972473856e-07,1.3798418576500274e-07,1.421640207192852e-07,1.4626310020369494e-07,1.5048462814793445e-07,1.5498941007992583e-07,1.59259111415505e-07,1.658872095439914e-07,1.7056793474682503e-07,1.7536441824065518e-07,1.8037506248250185e-07,1.851099955685805e-07,1.8994632997486698e-07,1.9438989998957098e-07,1.9859063750244262e-07,2.0289811265062994e-07,2.070605151575342e-07,2.136886067957609e-07,2.1829599903051246e-07,2.2265031036327405e-07,2.2725691351357784e-07,2.3197704635176555e-07,2.3640871082944755e-07,2.404522872491661e-07,2.445969266805802e-07,2.4858122001356486e-07,2.526558872819315e-07,2.587382166508494e-07,2.628365068041148e-07,2.6690714658682413e-07,2.7117882939283896e-07,2.754571638663946e-07,2.7985037747328125e-07,2.840027925979882e-07,2.879384547518487e-07,2.918850037079846e-07,2.958651118849987e-07,3.018666989617649e-07,3.062085691207088e-07,3.108935347345502e-07,3.1533816118127597e-07,3.200324977563818e-07,3.248304470020247e-07,3.295439333362772e-07,3.338324205734492e-07,3.3789709885284347e-07,3.4055574970438864e-07], marker='o', color='#7fa1ea', markerfacecolor='None',markeredgecolor='#7fa1ea', markeredgewidth=0.8)
plt.plot(x, [1.35543090368025e-08,2.729527718906063e-08,3.4024029656993846e-08,3.913902256744665e-08,4.3562161672687155e-08,4.7797310371492267e-08,5.182086834927337e-08,5.5694545759417316e-08,6.137180416104342e-08,6.452610245620852e-08,1.0579988090940297e-07,1.1425361252976187e-07,1.201441059102058e-07,1.249419290042774e-07,1.286561351296349e-07,1.3240043488104908e-07,1.3606714828189318e-07,1.3975874097065914e-07,1.434109745202031e-07,1.47056869672767e-07,1.5515666252137142e-07,1.5952211869676268e-07,1.63239705989492e-07,1.6694553034361785e-07,1.7060151695730867e-07,1.7420572508422845e-07,1.778717313544831e-07,1.8148720851317523e-07,1.8506384129798206e-07,1.8866716419524908e-07,1.952095817616404e-07,1.9899102364482132e-07,2.0274903533610906e-07,2.0650365320728076e-07,2.1030114109877845e-07,2.1393946875797934e-07,2.1764881460768503e-07,2.2128458531805234e-07,2.2483186918947758e-07,2.2842537629846794e-07,2.337947317637062e-07,2.3753546087641498e-07,2.411380719361725e-07,2.447147039423024e-07,2.483033479057945e-07,2.5196751101282966e-07,2.556018472995673e-07,2.5925568216001677e-07,2.629441195692501e-07,2.6652141666515897e-07,2.7228595978595093e-07,2.763688334895565e-07,2.8052012739895724e-07,2.845167999954824e-07,2.885267735678856e-07,2.9221851570834424e-07,2.959189465758115e-07,2.995399741205053e-07,3.034296085704542e-07,3.0562735037939647e-07], marker='o', color='#ff0000', markerfacecolor='None',markeredgecolor='#ff0000', markeredgewidth=0.8)
plt.plot(x, [1.89743971445784e-08,3.657583029864646e-08,4.465213114168971e-08,5.0014987633500045e-08,5.519792125461851e-08,6.045252263471174e-08,6.563701649856382e-08,7.160317502651717e-08,7.620282073692211e-08,8.039859657170106e-08,1.280547703919715e-07,1.3766291543086844e-07,1.4366994448038497e-07,1.4885723552419883e-07,1.5390194901349622e-07,1.5868489898528307e-07,1.634041514107616e-07,1.6832466269069413e-07,1.7343801868546505e-07,1.7853058791747688e-07,1.863187420564865e-07,1.9134524612815803e-07,1.964744922207364e-07,2.0164821773163784e-07,2.07223569051316e-07,2.1216356583326223e-07,2.1694769905330406e-07,2.2172830485408664e-07,2.268782409614701e-07,2.3185072773267428e-07,2.3973665857963984e-07,2.4615372002406146e-07,2.520453909020662e-07,2.573643712101724e-07,2.626458164210694e-07,2.6729653115752704e-07,2.717975904465959e-07,2.7633250976504305e-07,2.808383018864925e-07,2.86215671120267e-07,2.940574764611655e-07,2.9891301037184273e-07,3.0351660009778827e-07,3.0810105441632974e-07,3.127751387241574e-07,3.1775877247462215e-07,3.228842226377141e-07,3.277201256003876e-07,3.3221241474493345e-07,3.3688922644382276e-07,3.4400763063333654e-07,3.4929290027011326e-07,3.5451509047004225e-07,3.6056936412836904e-07,3.660775557432899e-07,3.712342165328695e-07,3.7648996558192925e-07,3.813058942636108e-07,3.8612388013505936e-07,3.8878336286216417e-07], marker='o', color='#000000', markerfacecolor='None',markeredgecolor='#000000', markeredgewidth=0.8)
plt.plot(x, [1.5029210559222847e-08,3.183570376568743e-08,4.086881858027934e-08,4.672936424445133e-08,5.1951275584141626e-08,5.7583041108218534e-08,6.311337868575463e-08,6.896169711935894e-08,7.340142656014487e-08,7.749093783913305e-08,1.2408228716808807e-07,1.3571204407413306e-07,1.4247895407749463e-07,1.472806816707245e-07,1.5183763680260463e-07,1.5654697722285244e-07,1.6115927084841914e-07,1.6565471291200837e-07,1.7039578096478763e-07,1.75027190333104e-07,1.813777196756299e-07,1.8616025497662673e-07,1.9097124462812563e-07,1.9711084544316162e-07,2.0301007460539644e-07,2.0816951415704147e-07,2.1300104011675052e-07,2.1732207161466196e-07,2.2204957409075317e-07,2.2671759195089444e-07,2.3316578287139826e-07,2.3736041623746958e-07,2.4145440672521524e-07,2.4629528380966086e-07,2.512784442107543e-07,2.557761339874046e-07,2.6052001237500356e-07,2.651694298998049e-07,2.70342050358324e-07,2.7504842645042885e-07,2.8118215770759187e-07,2.85734924835424e-07,2.90498418035621e-07,2.9493496066689016e-07,2.9955170707396377e-07,3.043201121605498e-07,3.0903855458325854e-07,3.1367907126922736e-07,3.1845717975364957e-07,3.228337818351705e-07,3.2960513025762784e-07,3.362905852296168e-07,3.41812882483477e-07,3.4632565427457607e-07,3.514028093571893e-07,3.557118846124721e-07,3.6014204071612176e-07,3.641422048316633e-07,3.679457351689157e-07,3.705567715746585e-07], marker='o', color='#ffcc66', markerfacecolor='None',markeredgecolor='#ffcc66', markeredgewidth=0.8)
plt.legend(['NB', 'Chi-Squared', 'FCBF', 'EFS', 'IG', 'OFS'], fontsize='small', shadow=True, fancybox=True)
plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Memory Consumption (RAM-hours)', fontsize=12)
np.arange(100, 7100, step=1000)
plt.tight_layout()
plt.savefig('memory_usenet_recurrent_1000.eps')