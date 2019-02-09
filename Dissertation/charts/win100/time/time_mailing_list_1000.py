import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-darkgrid')
x = np.arange(100, 6100, 100)
plt.plot(x, [1.7794532379999999,4.1986011114,6.449237977299999,8.6536265191,10.861846961600001,13.146989611999999,15.408320758200002,17.6650530427,20.016282050199997,22.326843846499997,24.6818239262,27.0079963457,29.2665336523,31.557583239200007,33.81870228340001,36.098548682700006,38.3656113899,40.6563509649,42.9907121253,45.3331357947,47.6353852786,49.9151768366,52.198211071399996,54.53923187939999,56.88995712909999,59.18211437110001,61.479595176299995,63.76585178199999,66.09693864559999,68.3997308556,70.7369713343,73.057121404,75.4263940305,77.7712979112,80.1624835409,82.4855638739,84.80605549790002,87.19322577710001,89.6138145797,91.97335249199999,94.3546740839,96.72583202130001,99.0472100624,101.38451520590002,103.70341420380001,106.0016755425,108.3307473762,110.6986643018,113.1065476488,115.490109953,117.81538921660001,120.14569064700001,122.51666701799999,124.9029761967,127.28143658709999,129.6426572331,131.9714860935,134.3650696575,136.71880903390002,138.94876395039998], marker='o', color='#996600', markerfacecolor='None',markeredgecolor='#996600', markeredgewidth=0.8)
plt.plot(x, [2.4011950329,5.9832925674,8.9527577294,11.9154062333,14.779926961799998,17.5892513904,20.399208465600005,23.244057163499996,26.105538095500002,28.902533748900005,31.724033512700004,34.488933747199994,37.2862029948,40.0777930749,42.8863359674,45.762055591700005,48.584101834900004,51.350323825500006,54.1024167399,56.91996540229999,59.69937145,62.51110566289999,65.30197361340001,68.1036334978,70.9487488572,73.8023113624,76.5638972462,79.3816829547,82.24396922349999,85.0434532594,87.84606972739999,90.6532282419,93.4970448789,96.2775924975,99.07412305110002,101.8494850973,104.68425104010001,107.48974611830002,110.3028226851,113.12341411770001,115.943156836,118.71686484410002,121.53426016389999,124.34581183089999,127.14917949470001,129.9442863792,132.7402728009,135.5330149828,138.29818631019998,141.1758023156,144.0038281211,146.76390036720002,149.65840107260001,152.4674633695,155.26893197500002,158.06983948680002,160.909745032,163.7069595626,166.50887488770002,169.22847070440002], marker='o', color='#0bf933', markerfacecolor='None',markeredgecolor='#0bf933', markeredgewidth=0.8)
plt.plot(x, [2.9760157715,7.4868593687,11.3242675632,15.0850405881,18.651450863500003,22.2727498737,25.889028095699995,29.4229003965,33.0799836121,36.6209453515,40.095447146000005,43.651253437899996,47.2630223107,50.8358483782,54.330386518299996,57.7646098476,61.4341779438,65.1251881953,68.672809118,72.16647367099999,75.79575395910001,79.25599305509999,82.81747145759998,86.3766821872,89.908468202,93.59500264229999,97.2389033312,100.82379096269999,104.34355118439998,107.9470913683,111.58317316539998,115.26331884259999,118.8498076072,122.475459828,126.1447409059,129.6661331802,133.1673474363,136.72541352520003,140.4078157083,143.99330961790002,147.5631836303,151.1354073092,154.699963762,158.33684385520002,161.9106887696,165.4533809179,169.11433325369998,172.7383071239,176.2456767353,179.77699006150002,183.35542582359997,186.94261513060002,190.5676598649,194.22621639029998,197.880297075,201.4981223977,205.0814875597,208.72119221140002,212.43213576539998,215.94463290459998], marker='o', color='#7fa1ea', markerfacecolor='None',markeredgecolor='#7fa1ea', markeredgewidth=0.8)
plt.plot(x, [1.9694445592,4.9156938896,7.3528385114,9.7448228739,12.0818170334,14.428947936000004,16.794426879099998,19.1576789998,21.4990119623,23.856334006999997,26.2052166597,28.549295393900003,30.9348795479,33.287095186799995,35.643773449,37.9994653567,40.3672870003,42.719017128400004,45.0620481563,47.42176694050001,49.7755131951,52.1220994378,54.491177703000005,56.85446634030001,59.203498526400004,61.5684699154,63.98537793800001,66.42894204230001,68.7888777008,71.15566921729999,73.5067664144,75.8536924948,78.22645520159999,80.59043051779999,82.95371649360001,85.3283863397,87.7383624614,90.10129883879999,92.48329080399999,94.8481575103,97.2337386474,99.60980555709997,101.999926622,104.37582976219998,106.77905825510001,109.16421167889999,111.5846163083,113.98296762520002,116.4070839985,118.80798741930002,121.25553529199999,123.67861264180003,126.0695669335,128.4600888435,130.8470962085,133.2943854346,135.75414626600002,138.159090741,140.5582374429,142.8749729292], marker='o', color='#ff0000', markerfacecolor='None',markeredgecolor='#ff0000', markeredgewidth=0.8)
plt.plot(x, [3.028395904,7.6588761091999995,11.616736678999999,15.4445927443,19.215731791899998,22.9191216624,26.6677551492,30.371119216700002,34.1149068155,37.911172482,41.6770727767,45.398644994899996,49.1214170103,52.819216735,56.6142803875,60.3644468602,64.14698134569998,67.7972883786,71.3684768592,74.9658217462,78.7275820062,82.46990004709998,86.16081206560001,89.8435750371,93.52409158649999,97.23713414480002,101.0068108768,104.72773475200002,108.47504175239999,112.2051055463,115.9987114988,119.80785059469997,123.48888320840001,127.24548867569999,131.0374764386,134.80106920330002,138.5518970565,142.386148065,146.1660080275,149.8955948301,153.60248188079998,157.3931747365,161.18351212940001,164.9182637344,168.70884596090002,172.53578831559997,176.37724157899999,180.1577700935,183.9601283533,187.78596638130003,191.52786404300002,195.33589368320003,199.07159147169997,202.8690328763,206.7559019629,210.46579141079997,214.2101707203,217.87821519210001,221.44613278269998,225.01545937400002], marker='o', color='#000000', markerfacecolor='None',markeredgecolor='#000000', markeredgewidth=0.8)
plt.plot(x, [2.1036330334000004,5.2360683267,7.8715910139,10.4546481334,12.935645678699998,15.437225073799999,17.9152128836,20.378765893599997,22.864841534500002,25.312558986299997,27.7931309007,30.2693901064,32.755326886700004,35.2753500425,37.8050835728,40.291331443199994,42.8572124753,45.360790849,47.8941843189,50.4285668426,52.955401568800006,55.46241597230001,57.9834505596,60.51285207909999,63.04189193709999,65.5975382772,68.1340065181,70.6803549351,73.2077756521,75.74273798380001,78.2622010154,80.8418539679,83.45840833689999,86.01635652860001,88.57803050659999,91.21288842690001,93.85544943900001,96.4756783928,99.0767819656,101.72898643279999,104.44096787069998,107.15517121730002,109.7828308624,112.40720741589999,115.002281513,117.65722030049999,120.29960470789999,122.92023306109998,125.58882521930002,128.19782056590003,130.824640399,133.4499286458,136.0149028205,138.59058770660002,141.134455726,143.70742575000003,146.27555390440003,148.86177335809998,151.42026386679998,153.89925091429998], marker='o', color='#ffcc66', markerfacecolor='None',markeredgecolor='#ffcc66', markeredgewidth=0.8)
plt.legend(['NB', 'Chi-Squared', 'FCBF', 'EFS', 'IG', 'OFS'], fontsize='small', shadow=True, fancybox=True)
plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Time (s)', fontsize=12)
np.arange(100, 7100, step=1000)
plt.tight_layout()
plt.savefig('time_mailing_list_1000.eps')