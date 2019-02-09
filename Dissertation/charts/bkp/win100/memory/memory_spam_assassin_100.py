import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-darkgrid')

x = np.arange(100, 9500, 100)

plt.gca().set_color_cycle(['blue'])

plt.plot(x, [1.3733463038944796e-05,3.586919783176667e-05,5.70479958597174e-05,7.806853021918344e-05,9.897011688304947e-05,0.000119970632530982,0.00014140832768065153,0.00016269729399125815,0.0001839837014692206,0.00020508679861609588,0.000226256259526315,0.00024796010501653006,0.00026954753849314095,0.00029129142109784946,0.0003130865200223529,0.0003349627620381822,0.0003565846563220178,0.0003789504072569671,0.00040090845711516056,0.0004229132436825205,0.00044495347588921215,0.00046687281723758664,0.0004888457949784723,0.0005108059789047676,0.0005326558654270193,0.0005544880650138627,0.0005765356282758172,0.0005987717536597285,0.0006209877749620759,0.000642965960023244,0.0006648589330854338,0.0006868914337261797,0.0007089612722152303,0.0007310745726154043,0.0007533073240122999,0.0007750945744873627,0.0007969181227233293,0.0008187717151132828,0.0008407587072701299,0.0008628910162781382,0.0008852874209934745,0.0009078184164040427,0.0009300708842764811,0.0009524304217735631,0.0009752642362853331,0.0009974827877048526,0.0010194683532697205,0.0010413656732057228,0.001063711343026481,0.0010859386071173447,0.001108046109878662,0.0011305233134244065,0.0011529621374190917,0.001175101052945117,0.0011973730365574147,0.0012197746900441172,0.0012422173188974732,0.0012644780693406251,0.0012871344923580707,0.0013097126248735366,0.001332293299016474,0.001355090687466608,0.0013776412442686329,0.0014000727143129907,0.0014225012504796683,0.001444843585471983,0.0014675438093990363,0.0014902980313650077,0.001512962933934156,0.00153587070678128,0.0015587654000055622,0.0015814032636316706,0.0016040067646102562,0.0016268689506789141,0.001649744984024009,0.001672393638346415,0.0016950587049857587,0.0017178623441435961,0.001740427170231134,0.0017629400765736812,0.0017858067125363839,0.0018089019539184775,0.0018317879376211286,0.0018543623144540345,0.0018765225464212418,0.0018986558471210586,0.0019208436873160355,0.001943412127908988,0.0019659062791939535,0.001988525127982445,0.002010829312356121,0.002033106605557541,0.002055625897812724,0.00206592200872601
], marker="o", color='#996600', markerfacecolor="None",
         markeredgecolor='#996600', markeredgewidth=0.8)
plt.plot(x, [1.941668318364307e-05,5.2096544392486755e-05,8.235080995693053e-05,0.00011139392441919772,0.00013904900723193505,0.00016710566706807801,0.0001948402883085608,0.00022453408125125185,0.00025496339116336096,0.00028414842633464274,0.0003137313247342636,0.00034347255777039416,0.0003718693122535594,0.0004016913157832135,0.00043054629286560185,0.0004597456036354289,0.000489050004691425,0.0005185003895605887,0.0005482428476331426,0.0005775364402020903,0.0006078547829079353,0.0006380076272978954,0.0006676202898812569,0.0006973341621524496,0.0007261739715299302,0.0007553272592090356,0.0007849491375185672,0.0008163693110502933,0.0008456196935303431,0.0008763100450216686,0.0009047683788230041,0.0009347762062122039,0.0009631231585929149,0.0009932235076530963,0.0010203005024807948,0.0010499250749619086,0.0010796379814891465,0.001108385467580748,0.0011386303882298936,0.0011698188756139988,0.001199344952273354,0.0012294646875319853,0.0012584151501906413,0.0012881658869868607,0.0013167490766660696,0.0013458907594658723,0.0013762981277622769,0.0014060329624535207,0.0014361151394442406,0.0014674711756866281,0.0014979715737703187,0.0015282521665955407,0.0015573907583611864,0.0015874101242196088,0.0016177483606565825,0.0016489505375224087,0.0016790083397708604,0.0017087515333941137,0.0017383166912008144,0.0017668368979088956,0.0017966207717095301,0.0018258631180829228,0.0018558746880131358,0.0018839892500058728,0.001914369423742214,0.0019439314387512644,0.001973890823749513,0.00200391974134759,0.002034707226717617,0.0020639291246744144,0.002094829722238057,0.002125094322655097,0.002154798207925096,0.0021866840408555064,0.0022171559348636884,0.002247178486378767,0.002277908087166838,0.0023077200358598187,0.0023402097233767146,0.0023704106003132803,0.002401994480737174,0.0024315723245550177,0.002462281443003647,0.0024918943357694497,0.0025210219314888245,0.0025528042089781825,0.0025821896524065658,0.00261250543771042,0.002642574235141475,0.0026723560967273075,0.002700863030052647,0.002730420146237331,0.0027599138124256664,0.0027728366150947432], marker='o', color='#0bf933', markerfacecolor='None',markeredgecolor='#0bf933', markeredgewidth=0.8)
plt.plot(x, [2.176451253705418e-05,5.665960384545518e-05,8.86038682723081e-05,0.00011859555954495398,0.00014884724957394302,0.00017884949153353961,0.00020817980995015817,0.00023903243132578582,0.00026911810957279154,0.00029918363047539445,0.000329973189901148,0.00035977396441822234,0.0003904677492520228,0.00042071780898848626,0.0004515241717533393,0.00048162227728478174,0.0005115857801361903,0.000542713174529248,0.0005733448268488146,0.0006041017857054315,0.0006353844710519292,0.0006666937892121265,0.0006973367236900346,0.0007282324276579736,0.0007580457061257367,0.0007888942999973055,0.0008201273944899824,0.0008518601024866488,0.0008834726136425043,0.000914745708500792,0.0009463312025327086,0.0009774862972048897,0.0010084635547452552,0.0010404970875705852,0.0010720637793873616,0.0011039843663953241,0.0011355130397204395,0.0011670506196812132,0.0011978161117735802,0.0012297517113667711,0.0012615992012700759,0.0012933088632634847,0.001325214562617378,0.0013564034423399498,0.0013868243726299209,0.0014182846905814496,0.001449352788401833,0.001481419013830037,0.0015140852052041933,0.0015465814386360192,0.0015786737396823506,0.0016105223835688929,0.0016415506930561336,0.0016726087029839873,0.0017031639368553341,0.0017353588300162714,0.0017662663216280368,0.0017990501842032598,0.0018303387506320439,0.0018617593110156789,0.0018926680520780094,0.0019234257783493913,0.001955662840650858,0.001987089148069142,0.0020184287459964244,0.002049863001355233,0.002081384186355719,0.002111611439672039,0.002143133474632997,0.0021744571918432517,0.002206492473788027,0.0022385656423525918,0.0022700893208296496,0.002301837806036122,0.0023334864730874304,0.0023655244736320432,0.002397157607791519,0.002429222879309275,0.0024610484144749955,0.0024933686045317213,0.002524846727250994,0.002555630149119759,0.0025865892271392495,0.002617347902837629,0.0026484531429586964,0.002680065811818036,0.0027111499851386733,0.002742507816259336,0.0027734599691728564,0.002804519671219057,0.0028358532716265114,0.0028680026514093177,0.0028990471978013873,0.0029135509349840654], marker='o', color='#7fa1ea', markerfacecolor='None',markeredgecolor='#7fa1ea', markeredgewidth=0.8)
plt.plot(x, [1.5505038098773798e-05,4.130599715873875e-05,6.430037767461458e-05,8.704961005531563e-05,0.0001095739431301929,0.00013197175746905426,0.0001542858879266368,0.00017679722713040126,0.00019948330759407784,0.00022223247647805465,0.0002448711532669847,0.0002675821418788483,0.00029049090857820293,0.00031334203552326205,0.00033624727318578765,0.00035899055809316587,0.000381634106070719,0.00040449500147293787,0.00042740060443123876,0.0004503840866096094,0.00047324973394431973,0.0004961446961798026,0.0005189036778252436,0.0005418066970367987,0.0005645526953212997,0.000587339020571769,0.0006102546754049425,0.000633365954241961,0.0006562833814952963,0.0006792245363490292,0.0007021928670943669,0.0007250781179016306,0.0007480665074064847,0.0007710973743124165,0.0007942452603077615,0.0008173008408127166,0.0008404167981899418,0.0008634147929124805,0.0008864101195306341,0.0009094151056841862,0.0009324490338565993,0.0009554802574234696,0.0009784992426386187,0.0010014647030434584,0.0010243525416241046,0.0010474080750242953,0.0010704033174640272,0.0010935061354878431,0.0011166496847219074,0.0011397693888243114,0.001162871054619288,0.0011858987163465037,0.0012089206914428845,0.0012320433939858038,0.0012550298245663804,0.001278147445269933,0.0013011531587906926,0.0013243450219676284,0.0013473898939854903,0.0013704740407480954,0.00139346978819235,0.0014164814525250437,0.001439576937430137,0.0014626485888803388,0.0014856121639245884,0.001508609115854475,0.0015316163656059986,0.0015544031134688866,0.0015773173435623428,0.0016003679941376417,0.0016235820061416893,0.0016467844718553858,0.001670279632726799,0.0016935191367841464,0.0017167086245944124,0.0017401020144934046,0.0017634540731474926,0.001786794104194063,0.0018098890711958006,0.0018331285534364332,0.0018560870561920126,0.0018790317781503432,0.0019020420208086552,0.0019250438345987542,0.001948234235057068,0.0019713809654609824,0.001994573551219021,0.002017951035915941,0.002041223202066344,0.0020644431122233396,0.0020876611850234655,0.0021109049559826986,0.0021345650766000663,0.0021456124846011447], marker='o', color='#ff0000', markerfacecolor='None',markeredgecolor='#ff0000', markeredgewidth=0.8)
plt.plot(x, [2.6318134623039747e-05,6.932542284227815e-05,0.00010773591706036883,0.00014440000011012923,0.00018072626591030073,0.00021682674961410607,0.0002532619905764624,0.00029121133544777577,0.00032854712982768923,0.0003651235317972096,0.000402445980041304,0.0004381627758692404,0.00047452226811342204,0.000511693095533528,0.0005488140759228679,0.000587806087737204,0.0006252270796015018,0.0006629877866041802,0.0007010874199109482,0.0007381403075252901,0.0007767464757907768,0.0008143457950584032,0.0008530265602898692,0.0008913149088027549,0.0009293918831881314,0.0009685878726503954,0.0010071713498276485,0.001045645699944413,0.0010851167390438176,0.0011249128281920079,0.001163793656102226,0.001202515521999239,0.001241019793775559,0.0012799157935171192,0.0013177923784502487,0.0013562806470684087,0.0013944775194404079,0.0014334658864803913,0.0014714347265490633,0.001510977179855239,0.001549678506685043,0.0015882779661910238,0.001627659353227182,0.0016673819070898827,0.0017062626206774036,0.0017459150401013545,0.0017841905926662786,0.0018228415067614366,0.001862094829048289,0.0019011720182927215,0.0019396816377875094,0.0019787733893732915,0.0020183649176904127,0.0020571692670767108,0.002096071398156747,0.002135249417698022,0.0021741558210061095,0.0022134380451078075,0.0022532662882247174,0.0022929701307423966,0.0023307092002772334,0.0023696741621029795,0.002408666718948066,0.0024474666139299266,0.002486912035934304,0.002526541715865548,0.0025652597325392917,0.002604340721811445,0.0026437036755849633,0.0026826185967184194,0.002721533127371209,0.002760440555300328,0.0027991249654963583,0.002839044901995191,0.0028791041652622097,0.002919865487829008,0.0029599388711561577,0.0030004834823672455,0.003040608155563794,0.0030804055732651238,0.003120227150309195,0.003160724560574593,0.0032005731784937666,0.003240587431005184,0.0032807382182012345,0.00332068564836662,0.0033598756664104264,0.003399077879881069,0.003438343972828646,0.0034780687436489982,0.003518336660637907,0.003556582480222472,0.0035955866106355885,0.0036131941270170177], marker='o', color='#000000', markerfacecolor='None',markeredgecolor='#000000', markeredgewidth=0.8)
plt.plot(x, [1.8639895139537427e-05,5.0722413805582167e-05,7.960825791351253e-05,0.00010775285961095553,0.00013594422076681746,0.00016390603036977,0.00019225984714496625,0.0002201122977104659,0.0002478943097660612,0.0002757907789857807,0.0003028964512544445,0.0003303295526947213,0.0003569583011214398,0.0003836264055395283,0.00041050569127729303,0.0004378963684636245,0.000465196104862754,0.0004929383726224592,0.0005197964840634106,0.0005470835097731345,0.0005742494204711518,0.0006015029132616365,0.0006289248329208591,0.0006564847994160142,0.0006841390433046152,0.0007118297265494354,0.000739054707771097,0.000766155711051011,0.0007930600544742693,0.0008201322435490569,0.000846981104253378,0.0008739440883793872,0.000901128380274109,0.0009280657315485325,0.0009553968301349426,0.0009828168989301517,0.001010081796775477,0.001037674612210788,0.001065332993357736,0.0010925097006172404,0.001119588887829564,0.0011468539187672008,0.0011743497705335418,0.0012017152499289086,0.0012288180490860937,0.00125602528742501,0.0012832902468452852,0.0013104049376193665,0.0013375711055079319,0.0013647921483829549,0.0013921323531963065,0.0014193935499442725,0.001446858318376309,0.001474311533372225,0.0015021087320719318,0.001529736731422245,0.001557408998715774,0.0015853590486849007,0.0016131125344654791,0.0016409391595365013,0.0016687855291798147,0.00169665498819976,0.0017241962458119787,0.0017518019089252715,0.001779571676529381,0.0018075314768692635,0.0018351046615855727,0.0018627844240316784,0.00189053726576825,0.0019180663696513184,0.0019453627649769893,0.001973003492683018,0.0020007557773075294,0.002028566098142336,0.002056288939752216,0.0020841832418120017,0.0021121540591689195,0.002140234616006593,0.0021683997022916325,0.0021962572870904387,0.0022237720811377148,0.0022514946213386187,0.0022793049445636294,0.002307286683365306,0.0023350369274982704,0.0023631138435593947,0.002391002802027323,0.002418879895999138,0.002446672968666937,0.002474518122389372,0.0025021954041256882,0.0025296784390547587,0.00255718747093421,0.0025702681458806623], marker='o', color='#ffcc66', markerfacecolor='None',markeredgecolor='#ffcc66', markeredgewidth=0.8)


#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper le0t')
plt.legend(['NB', 'Chi-Squared', 'FCBF', 'EFS', 'IG', 'OFS'], loc='‘lower right', fontsize='small', shadow=True, fancybox=True)


plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Memory Consumption (RAM-Hours) (%)', fontsize=12)

#plt.grid(color='k', linestyle='-.', linewidth=0.4)
plt.xticks(np.arange(100, 11000, step=1000))
#plt.yticks(np.arange(40, 110, step=10))

plt.tight_layout()

#plt.show()
plt.savefig('memory_spam_assassin_100.eps')