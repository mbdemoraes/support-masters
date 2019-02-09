import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(100, 10100, 100)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.gca().set_color_cycle(['blue'])

plt.plot(x, [56.000000000000014,53.5,56.999999999999986,57.25,55.8,55.66666666666667,56.142857142857125,56.375,56.44444444444444,57.60000000000001,57.999999999999986,58.416666666666664,57.76923076923076,58.357142857142854,58.733333333333334,59.0,59.17647058823529,59.5,59.684210526315795,59.95,59.95238095238095,59.772727272727266,59.95652173913042,59.958333333333336,60.08,60.23076923076924,60.44444444444444,60.607142857142875,60.689655172413794,61.06666666666668,61.29032258064516,61.15625,61.3030303030303,61.29411764705882,61.3142857142857,61.416666666666664,61.54054054054053,61.710526315789465,61.8974358974359,62.02499999999999,61.97560975609757,61.92857142857143,62.06976744186046,62.272727272727266,62.2,62.39130434782608,62.468085106382986,62.60416666666667,62.83673469387755,62.86,62.843137254901976,62.80769230769231,62.9622641509434,63.0,63.14545454545454,63.28571428571429,63.210526315789465,63.1551724137931,63.28813559322033,63.28333333333334,63.42622950819672,63.61290322580645,63.63492063492062,63.78125,64.04615384615384,64.03030303030302,64.14925373134328,64.26470588235294,64.47826086956523,64.45714285714284,64.4507042253521,64.6111111111111,64.71232876712328,64.83783783783782,64.90666666666665,64.94736842105262,64.88311688311687,64.83333333333334,64.88607594936708,64.91250000000001,64.98765432098766,65.07317073170734,65.13253012048195,65.28571428571426,65.34117647058825,65.36046511627907,65.47126436781608,65.4318181818182,65.57303370786518,65.56666666666665,65.63736263736266,65.69565217391303,65.76344086021506,65.85106382978724,65.89473684210525,65.92708333333336,66.01030927835052,66.07142857142857,66.10101010101012,66.25999999999999
], marker="o", color='#996600', markerfacecolor="None",
         markeredgecolor='#996600', markeredgewidth=0.5)
#plt.plot(x, [56.000000000000014,47.5,50.33333333333332,50.74999999999999,50.199999999999996,50.0,49.42857142857144,49.5,49.77777777777778,50.0,49.454545454545446,49.83333333333333,49.692307692307686,49.64285714285715,49.800000000000004,50.18749999999999,50.235294117647065,50.27777777777778,50.05263157894738,50.24999999999999,50.09523809523809,50.22727272727274,50.869565217391305,50.79166666666668,50.76,50.88461538461538,51.07407407407407,51.32142857142857,51.310344827586206,51.39999999999999,51.61290322580645,51.625,51.45454545454545,51.41176470588236,51.457142857142856,51.6111111111111,51.567567567567565,51.605263157894726,51.53846153846153,51.60000000000001,51.70731707317073,51.47619047619047,51.581395348837205,51.727272727272734,51.57777777777777,51.69565217391305,51.574468085106375,51.5,51.469387755102034,51.55999999999999,51.72549019607844,51.82692307692308,51.75471698113209,51.814814814814824,51.89090909090909,51.98214285714285,52.03508771929825,51.93103448275862,51.93220338983052,51.89999999999999,51.9672131147541,51.95161290322581,51.8888888888889,51.875000000000014,52.03076923076924,52.09090909090908,52.08955223880598,52.13235294117648,52.1304347826087,52.12857142857142,52.154929577464785,52.2638888888889,52.28767123287672,52.35135135135134,52.45333333333333,52.5,52.584415584415595,52.6025641025641,52.60759493670885,52.575,52.5432098765432,52.658536585365866,52.74698795180724,52.80952380952381,52.87058823529411,52.87209302325583,52.9080459770115,52.95454545454545,52.92134831460673,52.966666666666654,53.054945054945065,53.0,52.956989247311824,52.8936170212766,52.96842105263157,52.84375,52.876288659793815,52.816326530612244,52.777777777777786,52.8
#], marker="o", color='#0bf933', markerfacecolor="None",
#         markeredgecolor='#0bf933', markeredgewidth=0.5)
#plt.plot(x, [56.000000000000014,51.5,51.33333333333333,51.0,52.39999999999999,54.16666666666667,53.0,52.75,52.33333333333333,52.60000000000001,53.81818181818183,54.25,53.92307692307692,53.64285714285715,53.266666666666666,53.125,53.11764705882352,53.33333333333333,52.89473684210526,53.14999999999999,53.33333333333333,53.09090909090908,53.086956521739125,52.58333333333333,52.64,52.69230769230769,52.37037037037037,52.46428571428572,52.41379310344827,52.39999999999999,52.41935483870968,52.125,52.33333333333333,52.352941176470594,52.171428571428564,52.19444444444444,52.270270270270274,52.605263157894726,52.58974358974358,52.55,52.6829268292683,52.71428571428571,52.9767441860465,52.70454545454545,52.466666666666654,52.39130434782608,52.08510638297872,52.1875,51.95918367346938,52.019999999999996,52.03921568627452,52.13461538461537,52.20754716981132,52.22222222222223,52.16363636363637,52.25,52.210526315789465,52.172413793103445,52.28813559322033,52.2,52.344262295081975,52.516129032258064,52.55555555555556,52.484375000000014,52.39999999999999,52.39393939393939,52.4179104477612,52.44117647058823,52.47826086956523,52.528571428571425,52.492957746478865,52.45833333333333,52.43835616438356,52.48648648648647,52.55999999999999,52.526315789473685,52.42857142857143,52.46153846153847,52.34177215189874,52.3875,52.41975308641976,52.390243902439025,52.40963855421687,52.392857142857125,52.44705882352942,52.43023255813954,52.47126436781609,52.42045454545455,52.42696629213482,52.36666666666666,52.41758241758242,52.41304347826086,52.40860215053762,52.425531914893625,52.35789473684211,52.29166666666667,52.31958762886599,52.3673469387755,52.29292929292929,52.290000000000006
#], marker="o", color='#7fa1ea', markerfacecolor="None",
#         markeredgecolor='#7fa1ea', markeredgewidth=0.5)
plt.plot(x, [56.000000000000014,53.5,53.66666666666667,52.5,52.0,50.33333333333332,49.85714285714285,50.125,49.33333333333333,48.300000000000004,48.9090909090909,48.91666666666668,48.846153846153854,48.42857142857143,48.39999999999999,48.25,48.58823529411766,48.33333333333333,48.52631578947369,48.39999999999999,48.238095238095234,48.0,48.21739130434782,48.41666666666668,48.60000000000001,48.57692307692309,48.962962962962955,49.07142857142856,49.51724137931034,49.966666666666654,50.09677419354839,50.09375,50.24242424242424,50.1764705882353,49.88571428571429,50.0,50.2162162162162,50.42105263157895,50.33333333333332,50.574999999999996,50.85365853658537,51.023809523809526,51.16279069767443,51.36363636363636,51.37777777777778,51.54347826086958,51.829787234042556,51.9375,52.0,52.10000000000001,52.33333333333333,52.38461538461537,52.47169811320755,52.6111111111111,52.89090909090909,53.08928571428571,53.315789473684205,53.241379310344826,53.22033898305085,53.25,53.44262295081968,53.58064516129032,53.65079365079366,53.640625,53.61538461538463,53.59090909090908,53.88059701492536,53.97058823529413,54.028985507246375,54.10000000000001,54.07042253521128,54.05555555555556,54.1095890410959,54.31081081081082,54.36,54.407894736842096,54.467532467532465,54.42307692307692,54.31645569620254,54.35000000000001,54.44444444444444,54.36585365853658,54.44578313253011,54.54761904761905,54.60000000000001,54.52325581395348,54.54022988505746,54.44318181818183,54.42696629213482,54.34444444444445,54.31868131868133,54.27173913043477,54.25806451612904,54.32978723404254,54.263157894736864,54.17708333333333,54.268041237113394,54.40816326530613,54.39393939393939,54.42999999999999
], marker="o", color='#ff0000', markerfacecolor="None",
         markeredgecolor='#ff0000', markeredgewidth=0.5)
#plt.plot(x, [56.000000000000014,51.5,51.33333333333333,51.0,52.39999999999999,53.5,52.42857142857143,52.25,51.222222222222214,52.0,53.272727272727266,53.91666666666667,54.0,53.57142857142857,53.2,53.5,53.58823529411764,54.1111111111111,53.578947368421055,53.2,53.23809523809524,53.0,52.69565217391305,52.66666666666667,52.88000000000001,53.153846153846146,53.37037037037037,53.5,53.172413793103445,53.2,53.22580645161291,53.1875,53.24242424242425,53.26470588235294,53.42857142857143,53.52777777777777,53.432432432432435,53.368421052631575,53.46153846153847,53.425,53.51219512195122,53.54761904761905,53.46511627906976,53.40909090909089,53.355555555555554,53.3695652173913,53.44680851063829,53.60416666666667,53.69387755102041,53.68000000000001,53.88235294117648,53.94230769230769,54.018867924528294,53.98148148148148,54.236363636363635,54.28571428571429,54.35087719298245,54.22413793103448,54.30508474576271,54.466666666666654,54.45901639344264,54.37096774193547,54.41269841269842,54.421875,54.53846153846153,54.484848484848484,54.46268656716417,54.51470588235294,54.579710144927546,54.62857142857142,54.61971830985915,54.66666666666667,54.72602739726027,54.82432432432432,54.89333333333333,54.89473684210526,54.81818181818183,54.769230769230774,54.88607594936708,55.000000000000014,54.96296296296295,55.000000000000014,55.060240963855435,55.08333333333333,55.11764705882352,55.18604651162791,55.160919540229884,55.06818181818181,55.112359550561806,55.15555555555555,55.26373626373628,55.29347826086956,55.322580645161295,55.32978723404254,55.421052631578945,55.42708333333333,55.4639175257732,55.520408163265316,55.515151515151516,55.58999999999999
#], marker="o", color='#000000', markerfacecolor="None",
#         markeredgecolor='#000000', markeredgewidth=0.5)
plt.plot(x, [56.000000000000014,53.5,54.33333333333333,54.0,51.60000000000001,51.66666666666667,52.42857142857143,52.125,52.33333333333333,52.8,52.63636363636364,52.5,51.846153846153825,51.42857142857143,51.13333333333333,51.0625,50.705882352941174,50.94444444444445,51.157894736842096,51.249999999999986,51.23809523809524,51.45454545454545,51.56521739130436,51.58333333333333,52.040000000000006,51.96153846153847,52.1111111111111,52.28571428571429,52.55172413793103,52.60000000000001,52.61290322580645,52.75,52.78787878787877,52.58823529411764,52.51428571428572,52.5,52.75675675675676,52.657894736842096,52.92307692307692,53.0,53.07317073170732,53.28571428571428,53.34883720930232,53.272727272727266,53.2,53.21739130434783,53.29787234042554,53.312499999999986,53.30612244897959,53.22000000000001,53.17647058823529,53.36538461538463,53.32075471698114,53.20370370370371,53.290909090909096,53.21428571428571,53.28070175438596,53.46551724137932,53.542372881355945,53.53333333333332,53.50819672131148,53.58064516129032,53.73015873015872,53.75,53.815384615384616,53.86363636363636,53.805970149253724,53.98529411764706,54.01449275362319,54.0,53.95774647887323,54.04166666666667,53.97260273972603,53.97297297297298,53.92,54.039473684210535,54.116883116883116,54.1025641025641,54.10126582278481,54.075,54.123456790123456,54.109756097560975,54.060240963855435,54.119047619047606,54.11764705882352,53.988372093023244,53.98850574712644,53.93181818181817,53.93258426966291,53.92222222222223,53.91208791208793,53.85869565217392,53.91397849462366,53.8936170212766,53.85263157894737,53.874999999999986,53.886597938144334,53.90816326530613,53.949494949494934,54.02999999999999
], marker="o", color='#ffcc66', markerfacecolor="None",
         markeredgecolor='#ffcc66', markeredgewidth=0.5)


#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper le0t')
#plt.legend(['NB', 'Chi-Squared', 'FCBF', 'EFS', 'IG', 'OFS'], loc='‘lower right', fontsize='small', shadow=True, fancybox=True)
plt.legend(['NB', 'EFS', 'OFS'], loc='‘lower right', fontsize='small', shadow=True, fancybox=True)

plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Accuracy (%)', fontsize=12)

#plt.grid(color='k', linestyle='-.', linewidth=0.4)
plt.xticks(np.arange(100, 11000, step=2000))
plt.yticks(np.arange(40, 110, step=10))

plt.tight_layout()

#plt.show()
plt.savefig('acc_incremental_drift_100.eps')