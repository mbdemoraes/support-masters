import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-darkgrid')
x = np.arange(100, 6100, 100)
plt.plot(x, [0.1028954879,0.2277251208,0.2944812573,0.3381824009,0.374507836,0.41078040590000003,0.44646551579999993,0.4828712722,0.5169444295,0.5459569207999999,0.5758245322000001,0.6143669966,0.6435930708,0.6728638207000002,0.7017568132,0.7311793913000001,0.7612547132,0.7904446013,0.8193729956999999,0.849657105,0.8790880258000001,0.9082852005000002,0.9377645998,0.9675529935,0.9972746983,1.0261743899,1.056846307,1.0861983208,1.1156127786,1.1447024493,1.1752077280999997,1.2037345092999998,1.2324294711000001,1.2624361051999997,1.2917583944,1.3198742166999997,1.3480052369000002,1.3764753633000002,1.4045285805,1.4329727398999998,1.4612326306,1.4894990501,1.5176553547,1.5457973846,1.5740287416,1.6027616765000001,1.6309817004,1.6592807371,1.6883337227,1.7164929985999997,1.7462560269999998,1.7767200411999997,1.8060545094000002,1.8367614321999999,1.8678441302999995,1.8971646036999996,1.9257633005000003,1.9545405108,1.9832888899,1.999986875], marker='o', color='#996600', markerfacecolor='None',markeredgecolor='#996600', markeredgewidth=0.8)
plt.plot(x, [0.17912268620000005,0.7100962687000001,0.8368202006999998,0.9111276224999999,0.9849222678000003,1.0598406974999999,1.1381717190999998,1.1968780649,1.2538122192,1.3108079294,1.3650880431,1.4270035668999999,1.4773834635000003,1.5369823008999999,1.6057905856999999,1.6654020195,1.7264315772,1.7800394964,1.8317025148,1.8845777487000004,1.9356005651000001,1.9865534557,2.0370901688000003,2.0925871346999996,2.151852988,2.2113838872000002,2.2746453755,2.3295886975,2.3870905877,2.4442131184999996,2.4994431638999997,2.5556089431999998,2.6102385765999996,2.6648513508,2.7205944229000005,2.7856960073,2.8484233789999998,2.9085000255000004,2.9615072447,3.0166049186999997,3.0689465138,3.1171657875000003,3.1663114320999997,3.2141144961999997,3.2633909299000003,3.3109481703,3.3602208775999998,3.4095678169,3.4593070351,3.5083573786000004,3.5532554284,3.5967184787,3.6437533962,3.6892971939000008,3.7418965838000005,3.7932999257000004,3.8491840682000005,3.8980170222000003,3.9437599514999997,3.9688671627999996], marker='o', color='#0bf933', markerfacecolor='None',markeredgecolor='#0bf933', markeredgewidth=0.8)
plt.plot(x, [0.17621234800000002,0.6789998193,0.8154696960999999,0.881163814,0.9416291158999999,1.0102508431000001,1.079567667,1.1388208071,1.1887671809,1.2429048993000003,1.3040702534,1.3789933935000003,1.4394596069999999,1.4948387829999998,1.5498978867000002,1.6060766395000001,1.6657098867999998,1.7277783934000002,1.7896887676,1.844592817,1.8982101957999997,1.9544776562,2.0143417375999997,2.0763807028000003,2.139169306,2.1956861427,2.2546039786999996,2.3108909762,2.3693147350999997,2.4257079643,2.4791323663,2.5306667328,2.5757371669999998,2.6183939624,2.6592412462000006,2.6977483251,2.7378088699000003,2.7764559273,2.8142343558999996,2.8529421896000002,2.8919480043,2.9318755342000005,2.973236685800001,3.0112220832,3.0530441833,3.0925769792999995,3.1340295942000003,3.1740663549000003,3.214126771,3.2532356336000006,3.291504539899999,3.3276349276999992,3.3649099121999995,3.4019785333000003,3.4415884441,3.4779628639999998,3.514592262,3.5509744176,3.5847217037000005,3.6042538419999994], marker='o', color='#7fa1ea', markerfacecolor='None',markeredgecolor='#7fa1ea', markeredgewidth=0.8)
plt.plot(x, [0.12335091489999998,0.5463140478,0.6459995691,0.7090738188000001,0.7648813409999999,0.8185565093000001,0.8771625751000002,0.9278060338999999,0.9774780100000001,1.0236176607999998,1.0692164693000001,1.12093354,1.1659592872000002,1.2098981191,1.2513667089,1.2945319742999999,1.336301867,1.3773174084000002,1.4169639688999998,1.4544227791,1.4921925174,1.5317774778,1.5721608483,1.6124890573,1.6491764573999999,1.6864392678999998,1.7252063029999998,1.7634407638000003,1.8016444467,1.8389047579,1.8767703454,1.9203492940999998,1.9611334017000002,1.9994263304,2.0394314822,2.0777987528999997,2.11574623,2.1534105043,2.188781241,2.225296026,2.2606897503,2.2970607156,2.3359928682,2.3715581297,2.4066796687,2.4418459034,2.4786367027,2.5141499322999996,2.5498660651,2.5853006868,2.6207996564,2.6563443563,2.6942309431000004,2.7317789829000003,2.7721210479,2.8080924487,2.8484652029,2.8857732764999997,2.9246389753999997,2.9506125821000007], marker='o', color='#ff0000', markerfacecolor='None',markeredgecolor='#ff0000', markeredgewidth=0.8)
plt.plot(x, [0.16209653140000002,0.6265065589000001,0.7391851125,0.8043851100999999,0.8701628106000001,0.9391189104999998,1.0170576966999998,1.0711479605,1.1225235962000002,1.1754348032,1.2247389058,1.2918079541,1.3538269756,1.4064042771999998,1.4624787928000003,1.5193724669,1.5784185693,1.6303399793,1.6810987149999999,1.7267356240000002,1.7720130963000003,1.8189822743000001,1.8677486004,1.9198168699,1.9711650136999999,2.0231237445000003,2.0718550821,2.119373726,2.1676348827999994,2.2194546993000004,2.2760005998,2.3292711718000003,2.3793130254999997,2.4258360964000003,2.4762846167,2.5301513236999997,2.5844306927000003,2.6292353693,2.6708165802,2.7108548057,2.7505531681999997,2.7890847273,2.8277629801999997,2.8659928392,2.9031744572999996,2.9409756011,2.9797874022,3.0180312781000005,3.0567225251,3.0964760955,3.1331783225,3.1710953974999994,3.2084550630999997,3.2463244528000006,3.2853178221999997,3.3246512811000004,3.3658663422000004,3.4102843979,3.4511386491,3.4734714669999995], marker='o', color='#000000', markerfacecolor='None',markeredgecolor='#000000', markeredgewidth=0.8)
plt.plot(x, [0.1332055983,0.5475061068,0.646935455,0.7047649685999999,0.7554018883,0.8117491088,0.8779084712999999,0.9209549609,0.9594827134000001,1.0018034638000002,1.0448765801,1.0974797116000001,1.1348938106,1.1736045941,1.2134531648,1.2522441674000002,1.290477928,1.3277759367,1.3651153995,1.4012140677,1.4380636249999998,1.4765439525000001,1.5130555721,1.5547341417999998,1.5962646248999999,1.6333261234999998,1.6728302369999999,1.7103802905000003,1.7479571320000002,1.7837710566999998,1.8202805708,1.8567699826000001,1.8939025364,1.9307145996,1.9690874678,2.0049704288,2.0420548111,2.0783944474,2.1150863655000003,2.1523394639999998,2.1910880162,2.2265983959999995,2.2619168111,2.2954194200000004,2.3285872447,2.3622696068,2.3972996826000004,2.4315988014000003,2.4648825585000003,2.4985248978000003,2.5337625969,2.5665766465,2.6010280399,2.6352143901,2.6719587321000002,2.7055128305000005,2.7407574840000004,2.7744238836,2.806833943,2.8257991845], marker='o', color='#ffcc66', markerfacecolor='None',markeredgecolor='#ffcc66', markeredgewidth=0.8)
plt.legend(['NB', 'Chi-Squared', 'FCBF', 'EFS', 'IG', 'OFS'], fontsize='small', shadow=True, fancybox=True)
plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Time (s)', fontsize=12)
np.arange(100, 7100, step=1000)
plt.tight_layout()
plt.savefig('time_usenet_recurrent_1000.eps')