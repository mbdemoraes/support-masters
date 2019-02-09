import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-darkgrid')
x = np.arange(100, 6100, 100)
plt.plot(x, [0.1028954879,0.2277251208,0.2944812573,0.3381824009,0.374507836,0.41078040590000003,0.44646551579999993,0.4828712722,0.5169444295,0.5459569207999999,0.5758245322000001,0.6143669966,0.6435930708,0.6728638207000002,0.7017568132,0.7311793913000001,0.7612547132,0.7904446013,0.8193729956999999,0.849657105,0.8790880258000001,0.9082852005000002,0.9377645998,0.9675529935,0.9972746983,1.0261743899,1.056846307,1.0861983208,1.1156127786,1.1447024493,1.1752077280999997,1.2037345092999998,1.2324294711000001,1.2624361051999997,1.2917583944,1.3198742166999997,1.3480052369000002,1.3764753633000002,1.4045285805,1.4329727398999998,1.4612326306,1.4894990501,1.5176553547,1.5457973846,1.5740287416,1.6027616765000001,1.6309817004,1.6592807371,1.6883337227,1.7164929985999997,1.7462560269999998,1.7767200411999997,1.8060545094000002,1.8367614321999999,1.8678441302999995,1.8971646036999996,1.9257633005000003,1.9545405108,1.9832888899,1.999986875], marker='o', color='#996600', markerfacecolor='None',markeredgecolor='#996600', markeredgewidth=0.8)
plt.plot(x, [0.149798592,0.29108036039999996,0.3705931692,0.41232307510000005,0.4529083359,0.4945578147,0.5373157698,0.5802519336999999,0.6138985383,0.6460247015,0.9530498217000002,1.0187751669,1.0620409985,1.1039122797,1.1396765627999998,1.1749593903000002,1.2088102979,1.2409445332000002,1.272926817,1.3048533538000002,1.3478134537,1.3795697513999998,1.4110303994,1.4432737204,1.4761538609,1.5086884755,1.5396468447,1.5708824412,1.6027185798,1.6336553376,1.6754865398,1.7075512993,1.7382592377,1.7692503739999998,1.8013107054,1.8320831027,1.8626935463999998,1.8930321734,1.9250324243999999,1.9567436440000001,1.9974975843000002,2.0289801945,2.0598865460000004,2.0908444652999996,2.1213364459,2.1521972647000003,2.1857054648,2.219317866,2.2517714754000004,2.2831714701,2.3219175447000002,2.3542762012000003,2.3875039974000005,2.4224157678999996,2.4629520554999997,2.4963667836,2.5298776393,2.5632755383,2.5948384578,2.6112345400000003], marker='o', color='#0bf933', markerfacecolor='None',markeredgecolor='#0bf933', markeredgewidth=0.8)
plt.plot(x, [0.15660484879999997,0.2937255264,0.3662795688,0.4110843389,0.45410715819999997,0.4983472698,0.5416275345999999,0.5875724839,0.6227855129,0.6599119998,0.9941862898,1.0535445378000001,1.0945205146,1.1337376662,1.1729281856000002,1.2091552067,1.2427307559999998,1.2769178381,1.3122023286,1.3481036857,1.3958093601,1.4329688991,1.4713642231000001,1.5083145036,1.5446596814,1.5837485964,1.6230744987999999,1.6582011649,1.6934306770999998,1.7308560282000003,1.7806370231000002,1.8153598251999998,1.8492005207999997,1.8864098749,1.9226731291999997,1.9569947679,1.9909126696000001,2.0237740382,2.0573712440999996,2.0923650616,2.1341406683999997,2.1704071598000003,2.2081506607000003,2.2442697045999997,2.2782970843999997,2.313081662,2.3482409505,2.3830929736,2.4167513184000002,2.4510604013,2.4925312598000002,2.5276529742999996,2.5654563721,2.602805038,2.6416064844,2.6773429078999995,2.7155796709,2.7483789038999995,2.7808202378,2.7984235575], marker='o', color='#7fa1ea', markerfacecolor='None',markeredgecolor='#7fa1ea', markeredgewidth=0.8)
plt.plot(x, [0.1217542251,0.2600817331,0.31895633069999996,0.36458163620000006,0.40667953209999996,0.4431565055,0.4788657926,0.513160707,0.5586934182000001,0.5867992608999999,0.8755245937000001,0.9332384215999999,0.9676760112,0.9995112618,1.0285053826000001,1.0582569184000001,1.0868057969,1.1149154369,1.1431170465,1.1714757472,1.2118915265,1.2403792935999998,1.2688864731,1.2974835747999998,1.3252688115999998,1.3538148204,1.3818766046,1.4096405626,1.437335219,1.4649364418,1.5032911510999998,1.5314838649999998,1.5594588119000001,1.587521177,1.6161480212000001,1.6438955343,1.6717737011,1.6999867331,1.7280236017,1.755721427,1.7924489178000003,1.8200888031000002,1.8476842456,1.8760113619999998,1.9038135273999999,1.9318158417,1.9599187155,1.9876686994000003,2.0155336222000004,2.044415422,2.0863190057,2.1184957720999997,2.1499125284000002,2.1801804350999996,2.2117639181,2.2440875724000002,2.2759064013,2.3058186684,2.3347024284,2.3501815060999998], marker='o', color='#ff0000', markerfacecolor='None',markeredgecolor='#ff0000', markeredgewidth=0.8)
plt.plot(x, [0.17144428520000002,0.3249124725,0.41596576030000004,0.46485668710000005,0.5106487768,0.5555016457999999,0.6007658813,0.6459598712,0.6853117269,0.7214807141999999,1.078520525,1.1517656209,1.196873661,1.2357813859,1.2727550407000001,1.3094509552,1.3482679311,1.3887194561,1.4273465582999998,1.4653802994999998,1.5158138898,1.5519916029,1.588893042,1.6259324919,1.6626191550999998,1.7003164800000001,1.7367243004000001,1.7725092291,1.8078008216,1.8458235632000002,1.8994227936,1.9346849013,1.9692620259999998,2.0044804706,2.0393174836,2.0761101874000003,2.1117021478,2.1473974081,2.1825001219999995,2.2185199119,2.2658551835000003,2.3056286892,2.3445321725,2.3830861409999997,2.4193000803,2.4558786313000005,2.4910918814,2.5259914578,2.5632265684999997,2.6003463513,2.6437108138000003,2.6795615506,2.719453884200001,2.7611308503,2.8075895403999995,2.8471371954999998,2.8839392975,2.9195024452,2.9525209969999997,2.9716085527000002], marker='o', color='#000000', markerfacecolor='None',markeredgecolor='#000000', markeredgewidth=0.8)
plt.plot(x, [0.16129666709999999,0.32478958430000004,0.41152475720000004,0.46698615870000004,0.5133417778,0.5593078120000001,0.6012172177,0.6542967017000001,0.7146809293999998,0.7936442589000001,1.178873945,1.2709645804999998,1.335385433,1.3972954235,1.4560782788000002,1.513491351,1.5669369960000004,1.6200208535999998,1.6791797013,1.7365152002000002,1.7970081642,1.8464145648000003,1.8952281101000001,1.9388922913999997,1.9878130103999996,2.0322418763,2.0708701691,2.1093714042,2.1493275542,2.1917965003999997,2.2395045793,2.2795680647000003,2.3221793593,2.3600109635999997,2.3983329040999997,2.439138122,2.4766799489,2.5118142552,2.5482522183000005,2.5851597823,2.6257210632,2.6620464427,2.7023197193000006,2.7435305893000006,2.7816418656,2.8206115415,2.8568735678,2.8928172450000003,2.9286810445,2.9637088103,3.0017957582,3.0362632926999997,3.0713378445000004,3.1077608835,3.147801476,3.1831626621,3.2204853852999995,3.2576486390999997,3.2966014243999995,3.3188190144], marker='o', color='#ffcc66', markerfacecolor='None',markeredgecolor='#ffcc66', markeredgewidth=0.8)
plt.legend(['NB', 'Chi-Squared', 'FCBF', 'EFS', 'IG', 'OFS'], fontsize='small', shadow=True, fancybox=True)
plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Time (s)', fontsize=12)
np.arange(100, 7100, step=1000)
plt.tight_layout()
plt.savefig('time_usenet_recurrent_100.eps')