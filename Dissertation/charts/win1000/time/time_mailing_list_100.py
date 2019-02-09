import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-darkgrid')
x = np.arange(100, 6100, 100)
plt.plot(x, [1.7794532379999999,4.1986011114,6.449237977299999,8.6536265191,10.861846961600001,13.146989611999999,15.408320758200002,17.6650530427,20.016282050199997,22.326843846499997,24.6818239262,27.0079963457,29.2665336523,31.557583239200007,33.81870228340001,36.098548682700006,38.3656113899,40.6563509649,42.9907121253,45.3331357947,47.6353852786,49.9151768366,52.198211071399996,54.53923187939999,56.88995712909999,59.18211437110001,61.479595176299995,63.76585178199999,66.09693864559999,68.3997308556,70.7369713343,73.057121404,75.4263940305,77.7712979112,80.1624835409,82.4855638739,84.80605549790002,87.19322577710001,89.6138145797,91.97335249199999,94.3546740839,96.72583202130001,99.0472100624,101.38451520590002,103.70341420380001,106.0016755425,108.3307473762,110.6986643018,113.1065476488,115.490109953,117.81538921660001,120.14569064700001,122.51666701799999,124.9029761967,127.28143658709999,129.6426572331,131.9714860935,134.3650696575,136.71880903390002,138.94876395039998], marker='o', color='#996600', markerfacecolor='None',markeredgecolor='#996600', markeredgewidth=0.8)
plt.plot(x, [2.1798304484,4.8810734984,7.4033896745000005,9.8997257552,12.365585866799998,14.8508665956,17.343377623800002,19.8149238287,22.3397344081,24.8683305557,27.798535882799996,30.2569692659,32.650282670299994,35.0779290672,37.47304263240001,39.883924158199996,42.3083937311,44.7170876187,47.154876413400004,49.588334256799996,52.1497471661,54.5486593361,56.9671816363,59.38567610890001,61.82179492319999,64.21195425869999,66.6310597349,69.05661827000002,71.5169887865,73.93168029580002,76.5112096681,78.9414523445,81.374158111,83.8122087716,86.25659172419999,88.6834120775,91.09921498949998,93.53383250399999,95.9799209933,98.3769738378,100.87786230840001,103.32508056900001,105.7180199871,108.12579518339999,110.52012914669999,112.9193566493,115.31226734750001,117.7359537868,120.16364947450002,122.57829474999998,125.05427944789999,127.45522323949999,129.86264339989998,132.29031462289998,134.6897745617,137.08630293750002,139.4908530695,141.89892823609998,144.2918616603,146.5718236676], marker='o', color='#0bf933', markerfacecolor='None',markeredgecolor='#0bf933', markeredgewidth=0.8)
plt.plot(x, [2.4406902128000003,5.683792810199999,8.7532073101,11.7447468883,14.743728266100002,17.6944945597,20.6557322818,23.5570595691,26.356508756999993,29.284145740899998,32.6244960346,35.4370594745,38.196462386899995,40.9243534679,43.7085135075,46.4386580119,49.1863572871,51.8826736612,54.57872186640001,57.224373464799996,60.069139486000005,62.7548311771,65.42000496529998,68.1188635494,70.8321760586,73.602440514,76.2775463954,78.9076779734,81.57138488160001,84.36477624669999,87.2323750633,89.90761289999999,92.6805544651,95.49716528270002,98.2079192438,101.0506497642,103.84552404039998,106.58850477390001,109.43132010929999,112.17560525619999,115.02808344320002,117.82314280090002,120.5477301312,123.35947681820002,126.1925776573,128.99751975650003,131.7778715018,134.57275825440001,137.3651064027,140.222557466,143.1006690209,146.0531547219,148.9541583511,151.82750061549999,154.7551082319,157.6818202077,160.49972346520002,163.37789771169997,166.24174128910002,168.91236380380002], marker='o', color='#7fa1ea', markerfacecolor='None',markeredgecolor='#7fa1ea', markeredgewidth=0.8)
plt.plot(x, [1.8214615381,4.2525466210000005,6.4770145159000005,8.705070216699998,10.9225031038,13.149352019,15.388577697999997,17.635131389900003,19.8804353807,22.1383031178,24.643627803799998,26.8146989939,28.9691243152,31.1242836608,33.2868169977,35.444137215,37.606013449,39.7651770438,41.928713378,44.0958118768,46.30849286269999,48.47135420539999,50.6451702443,52.819380441300005,54.9895958856,57.158949496299996,59.385407704200006,61.6578844096,63.8450952807,66.0250832469,68.2494662359,70.42585636049999,72.60639972540001,74.78390578060001,76.9670345894,79.14922160110001,81.3325480654,83.51199488149999,85.6944125588,87.8741273119,90.0955933397,92.28055246779999,94.4678961577,96.6529228158,98.83705732170002,101.02174392239999,103.2108831169,105.3914401473,107.58178201090001,109.77045644870002,111.98251457730001,114.1697595713,116.3589561071,118.55788096770002,120.75167869719999,122.9445213852,125.1260429416,127.31490521510003,129.510756086,131.5982444686], marker='o', color='#ff0000', markerfacecolor='None',markeredgecolor='#ff0000', markeredgewidth=0.8)
plt.plot(x, [2.8285375101,6.499325612000002,10.038815287099998,13.499981734700004,16.8368796453,20.1408837449,23.494941444400002,26.9370287601,30.197707613699997,33.5019087199,37.2916530783,40.5947425664,43.7859028341,46.89913751180001,50.10166998360001,53.486911125999995,56.56284157719999,59.909747338,63.138814370400006,66.335109818,69.79586030979999,72.9587264562,76.24722267439999,79.55942949620001,82.77423297979999,86.0618508545,89.3725167708,92.54626722239998,95.80458723720001,98.87829622419999,102.17209240470001,105.3331850691,108.4183130741,111.5832749168,114.75199474450001,117.81076240630003,121.04016406859998,124.3158934458,127.50707967590002,130.75639158750002,133.99333685780002,137.05331513800002,140.24221920929998,143.2735741192,146.42723940690001,149.66328038339998,152.8899240545,155.9737319075,159.2444931625,162.27652034899998,165.4517257892,168.53266658080003,171.5984420789,174.707175199,177.715718653,180.78676867080003,184.05598795270004,187.26246010929998,190.4008981325,193.42565528979998], marker='o', color='#000000', markerfacecolor='None',markeredgecolor='#000000', markeredgewidth=0.8)
plt.plot(x, [2.1451365975999996,4.9087391406,7.493503228699998,10.066848897800002,12.6246008666,15.167355788999998,17.7327610192,20.328222915100003,22.8827958404,25.4520762876,28.2578517525,30.7410360503,33.2085596219,35.6772105402,38.076848158000004,40.5031298146,42.9157475591,45.347310883999995,47.7456476493,50.177207458599995,52.6850266684,55.1314825013,57.5790762654,60.0022816068,62.491761394,64.9379364248,67.3574085535,69.81860677329999,72.27896234379999,74.70551786690001,77.1814166777,79.6009995733,82.059930519,84.46921282209999,86.8787078939,89.3183582849,91.74102104789999,94.1540522025,96.5739331339,99.0075742112,101.48650546610001,103.9366583301,106.3571958992,108.76972988119999,111.1977295792,113.64702668879997,116.06029715109999,118.49602326590002,120.9447458528,123.37455791740001,125.85694244250001,128.31543597419997,130.74494407950002,133.20078193909998,135.6482625882,138.0801826806,140.5076510602,142.89417455569998,145.3251055944,147.66271459709998], marker='o', color='#ffcc66', markerfacecolor='None',markeredgecolor='#ffcc66', markeredgewidth=0.8)
plt.legend(['NB', 'Chi-Squared', 'FCBF', 'EFS', 'IG', 'OFS'], fontsize='small', shadow=True, fancybox=True)
plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Time (s)', fontsize=12)
np.arange(100, 7100, step=1000)
plt.tight_layout()
plt.savefig('time_mailing_list_100.eps')