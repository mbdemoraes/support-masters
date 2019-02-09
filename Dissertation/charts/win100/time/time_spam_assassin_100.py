import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-darkgrid')
x = np.arange(100, 9500, 100)
plt.plot(x, [2.2316790095999997,5.599749518,8.8204408605,12.016226568399999,15.193271818300001,18.384549310700002,21.6403990918,24.8678724737,28.092753145,31.288661875000003,34.4933904981,37.7780829348,41.044540585099995,44.333412547399995,47.6293533133,50.936993518099996,54.2057338174,57.5854573644,60.90313162090001,64.2274214864,67.5563397723,70.86669366899999,74.1847867484,77.50026417059999,80.79874514999999,84.09406294270002,87.42130533310001,90.7765566315,94.12794200519998,97.4429610939,100.7447050436,104.067307035,107.39521860680001,110.72955587599999,114.0817776621,117.366627669,120.65662179199998,123.95098496550001,127.26534196200001,130.6014002917,133.97690876689998,137.3726029928,140.7261160628,144.09564606089998,147.53645766329998,150.884400265,154.1971177353,157.49335743370003,160.85685367170004,164.2023978744,167.52967579379998,170.9124293517,174.28928455989998,177.62072051619998,180.97177998479998,184.3420530098,187.7183479061,191.0671609186,194.4752972933,197.8712247522,201.26730341559997,204.6957410556,208.0869084552,211.46006073520002,214.832580146,218.19170860539998,221.604484921,225.0251002055,228.43215031740002,231.87550159850002,235.3167660715,238.7193386897,242.1163565412,245.5522106754,248.99005726549998,252.39366541169997,255.7996037849,259.22632186630005,262.6170783845001,265.99989639290004,269.43577030049994,272.9059171926,276.3445407299,279.73501678209993,283.0631946118,286.387270805,289.71946863830004,293.10870970630003,296.4866628660001,299.8831521388,303.2321586114,306.5770242956,309.9579434624,311.5037372338], marker='o', color='#996600', markerfacecolor='None',markeredgecolor='#996600', markeredgewidth=0.8)
plt.plot(x, [3.1551393992,8.126311657299999,12.725973663400001,17.1403215316,21.342826803,25.6052806379,29.816401102000004,34.316930659,38.9257943968,43.34454114560001,47.8218092091,52.3217622633,56.6174802665,61.1270775116,65.4895464995,69.9033132811,74.33236595729998,78.78154604179998,83.27425423519999,87.6985661065,92.2766508118,96.8293253368,101.2999534681,105.78493641309998,110.1375348924,114.53678650100001,119.00596714630001,123.74583208530001,128.1572798164,132.78521851419998,137.07603221489998,141.6002198126,145.87359109330004,150.4111168903,154.4927282547,158.95809177569998,163.4363230274,167.7688387097,172.3268720409,177.0268180776,181.47577667180002,186.0140536297,190.3758866118,194.8581348592,199.16424123820002,203.5542848733,208.13483669919998,212.60976079489996,217.13664357980002,221.8550396077,226.4443486088,231.00036071359995,235.3843895911,239.90054288610003,244.46412368780003,249.1572475506,253.67805741659998,258.151388781,262.5976836558,266.886282929,271.364596654,275.76118496500004,280.27322692550007,284.49993202490003,289.06698725340004,293.5104807301,298.0134927334,302.5265871223,307.1535003311,311.5448635736,316.18833419569995,320.7361135565,325.1991240284,329.9899151672,334.5681465318,339.07877743439997,343.6954518226,348.17420498650006,353.055135736,357.5920342905999,362.33656085030003,366.7796427363,371.39255129180003,375.83905206369997,380.21255514070003,384.98457624689996,389.3966281136,393.9482098642,398.46253329340004,402.93352843569994,407.2128283264001,411.64963954509994,416.07655732059993,418.0162267232], marker='o', color='#0bf933', markerfacecolor='None',markeredgecolor='#0bf933', markeredgewidth=0.8)
plt.plot(x, [3.2211409159999995,8.032173848,12.4288085594,16.5459016063,20.7227425938,24.854532521500005,28.8868347025,33.112954657299994,37.2088872363,41.319070879899996,45.531240360599995,49.59021099180001,53.803844241,57.9272149379,62.148463451599994,66.2567177777,70.3424836236,74.6001006237,78.77785633689999,82.98075670229998,87.24665145270001,91.5186730343,95.6977810923,99.91265269370001,103.9769128291,108.19206452320002,112.45742065169998,116.7704489166,121.09700342900001,125.35002573899999,129.6832594265,133.9280011063,138.1705623099,142.5457588578,146.89599256629998,151.26090483239997,155.56498203229998,159.8847419266,164.06542699550002,168.4079668595,172.76182033269998,177.0858341152,181.456738019,185.70743471589998,189.85979184950003,194.16012098020002,198.3821472934,202.7604373952,207.22348173400002,211.64161000160001,216.01151507050002,220.3478517341,224.5777908304,228.7985841219,232.93844829390005,237.31157737920003,241.5081029666,245.99141339899998,250.25226180529998,254.5481288996,258.7477466678,262.9325137383,267.3279396176,271.62985756060004,275.8844378544,280.1649999805,284.4524555686,288.5440484152,292.8186625949,297.0867434985001,301.4363773991,305.8011477447,310.0912837784,314.3823625525,318.6795770606,323.04195110859996,327.33270386320004,331.7021110002999,335.99517822539997,340.39676463210003,344.6509569543,348.83083369279996,353.0200043261999,357.1939036792,361.4270044971,365.69636275489995,369.9222686192,374.175148687,378.37066585680003,382.5864018052,386.8621003641,391.24435970449997,395.4613739133,397.44437164849995], marker='o', color='#7fa1ea', markerfacecolor='None',markeredgecolor='#7fa1ea', markeredgewidth=0.8)
plt.plot(x, [2.1658916454000003,5.559916134800001,8.5702316339,11.572167797899999,14.535355223899998,17.4823636395,20.425185584900003,23.3695574898,26.350001786100005,29.3391844944,32.2995390038,35.284954920400004,38.2862174076,41.2843258042,44.281588115800005,47.2645577959,50.234083382600005,53.21756989840001,56.214901894499995,59.2217019617,62.202114016500005,65.1862754396,68.1596435719,71.15032462399999,74.13333172950001,77.1063547853,80.09256962059999,83.1003605986,86.0799813613,89.0678605125,92.0547446244,95.0354260125,98.0340497341,101.02303853000001,104.0365917437,107.03071356769999,110.03954341529997,113.03031419869998,116.03221431079999,119.01775332279999,122.00866540199999,125.00115904099998,127.98867312539998,130.97881755650002,133.9686714622,136.96799117289999,139.96403040769997,142.9583497475,145.94956194039997,148.93962792459996,151.932841628,154.91843935,157.91541614959996,160.9268424348,163.9249738398,166.9179112126,169.91325367160002,172.9082651959,175.90348322990002,178.9022410498,181.895199313,184.8926163837,187.88026186800002,190.87641837970003,193.8574613247,196.8417172906,199.8260752279,202.79649590160003,205.76649650130003,208.7597993612,211.7668539593,214.7715256174,217.82808700790002,220.84282184119996,223.8514638084,226.88483148929998,229.91795155150004,232.9427327543,235.93423213280002,238.9398896211,241.91590329100003,244.90021687540002,247.891663557,250.88368242039996,253.89872689819998,256.8995437461,259.9151183482,262.9542421746,265.9835265531,269.0031818441,272.0182404252,275.0248180215,278.11022292800004,279.5507316965], marker='o', color='#ff0000', markerfacecolor='None',markeredgecolor='#ff0000', markeredgewidth=0.8)
plt.plot(x, [4.024651888299999,10.1743324046,15.664426947900001,20.8913406971,26.0692518775,31.2134779418,36.406862487699996,41.817447195599996,47.12876643310001,52.3221711958,57.6281690097,62.688624563199994,67.84235700050002,73.117677986,78.38356003060001,83.93380612989998,89.24736664870001,94.60665475389999,100.0157515853,105.26485311679998,110.74913527880001,116.0804484758,121.57650107879999,127.01001540569999,132.41343139010002,137.9842908099,143.45981241090004,148.9151906914,154.5224563873,160.1775558886,165.6935232364,171.1864705595,176.6445306187,182.1607926055,187.5214147535,192.9753023712,198.38381730679998,203.9131326433,209.28864801260002,214.90082488980002,220.38523220889996,225.8541706918,231.4407705339,237.0793802033,242.59202154299996,248.2181340588,253.63754432579998,259.1066011952,264.66531797470003,270.1976747593,275.6445060664,281.1797703453,286.7901138501,292.2800355301,297.78606113940003,303.3311249191,308.836784942,314.3959711146,320.03915823649993,325.6623303045,330.9910260744001,336.50343075829994,342.01848042750004,347.5047488495,353.089376981,358.70048539280003,364.17415055890007,369.7052336901,375.27655251799996,380.7781563007,386.27705491790005,391.7749160797,397.2342401937,402.8829768482,408.5532522668001,414.3258298527,419.9954457088,425.73596247740005,431.416946725,437.0463686970999,442.68348324439995,448.42220179670005,454.06234342310006,459.7252739193,465.4057080435,471.0561672559,476.5920992722,482.1268970237999,487.67265142290006,493.2877391223001,498.98399948569994,504.3761621436,509.8754470486,512.3524601223], marker='o', color='#000000', markerfacecolor='None',markeredgecolor='#000000', markeredgewidth=0.8)
plt.plot(x, [2.6013088084,6.8274830548,10.635210498400001,14.3558010035,18.0878640738,21.787545775999995,25.539554788900002,29.185907998599998,32.8283960009,36.4983441216,40.0359057552,43.6462994799,47.124607953499996,50.5952685551,54.097897642700005,57.6489422837,61.20950573350001,64.8302445672,68.3118247603,71.87352950510001,75.3927134012,78.93999926170001,82.49600042310001,86.0780287262,89.6771024676,93.2642502696,96.7897483054,100.29771742579999,103.76012596259997,107.24243460390001,110.7044247776,114.1858257314,117.703534766,121.17797728500003,124.72701078080001,128.28001908689998,131.81367731920002,135.38465607350003,138.9807563178,142.4803353919,145.9775242425,149.5041479923,153.053553548,156.5780515931,160.0754627114,163.57681931129997,167.1074881787,170.60648937320002,174.10392872960003,177.6121411323,181.1465706158,184.66017951450002,188.1967708377,191.74316275619998,195.3394051582,198.9057312058,202.4826497679,206.0955668011,209.6704988954,213.25784481390002,216.87745919589997,220.4818656877,224.0363541594,227.60330915480003,231.18502809349997,234.79208397789998,238.35456350750002,241.92731437380002,245.5066661486,249.0589117745,252.57606945380002,256.14498488579994,259.7336034663,263.3123357211,266.8757387454,270.4542837737,274.0545173955,277.6641113075,281.29263351239996,284.879730293,288.4148687879,291.9709844378,295.5499483694,299.1507630504,302.7146628859,306.3306050615,309.9296229965,313.5265534517,317.10977051110007,320.6937199556,324.2440670482,327.79550028079996,331.3391577322,333.03827316369996], marker='o', color='#ffcc66', markerfacecolor='None',markeredgecolor='#ffcc66', markeredgewidth=0.8)
plt.legend(['NB', 'Chi-Squared', 'FCBF', 'EFS', 'IG', 'OFS'], fontsize='small', shadow=True, fancybox=True)
plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Time (s)', fontsize=12)
np.arange(100, 10500, step=1000)
plt.tight_layout()
plt.savefig('time_spam_assassin_100.eps')