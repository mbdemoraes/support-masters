import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-darkgrid')
x = np.arange(100, 9500, 100)
plt.plot(x, [100.0,98.0,98.66666666666666,99.0,98.79999999999998,98.66666666666666,97.2857142857143,85.125,78.0,74.60000000000001,70.72727272727273,70.33333333333336,68.0,66.07142857142857,64.53333333333332,63.0625,61.76470588235294,61.277777777777786,59.73684210526316,59.8,58.333333333333336,57.09090909090911,56.913043478260875,56.79166666666667,57.2,56.230769230769226,55.29629629629629,55.07142857142857,54.48275862068965,54.06666666666666,54.12903225806451,54.03125,54.81818181818183,55.17647058823529,55.8,56.25,56.999999999999986,57.236842105263136,57.69230769230769,58.175,58.219512195121965,58.73809523809523,59.0,59.63636363636364,60.28888888888889,60.76086956521739,61.38297872340426,61.750000000000014,62.04081632653062,62.519999999999996,62.66666666666667,63.11538461538463,63.50943396226414,63.814814814814795,64.29090909090907,64.7142857142857,65.21052631578948,65.68965517241381,66.06779661016948,66.41666666666666,66.65573770491802,66.74193548387096,67.17460317460316,67.453125,67.8153846153846,67.92424242424241,68.31343283582089,68.38235294117648,68.73913043478261,68.97142857142856,69.35211267605634,69.69444444444444,69.87671232876711,70.25675675675676,70.60000000000001,70.98684210526315,71.18181818181816,71.55128205128203,71.81012658227847,72.0625,72.25925925925925,72.53658536585364,72.75903614457832,72.91666666666664,73.14117647058823,73.43023255813954,73.68965517241381,73.9431818181818,74.123595505618,74.21111111111112,74.4065934065934,74.55434782608697,74.53763440860213,74.57099957099958], marker='o', color='#996600', markerfacecolor='None',markeredgecolor='#996600', markeredgewidth=0.8)
plt.plot(x, [100.0,98.0,98.66666666666666,99.0,98.79999999999998,98.66666666666666,97.2857142857143,85.125,78.0,74.60000000000001,72.09090909090911,72.83333333333336,71.15384615384617,70.5,69.2,67.875,66.7058823529412,66.3888888888889,65.78947368421053,66.14999999999999,67.14285714285712,68.04545454545453,68.95652173913045,69.08333333333334,69.79999999999998,70.0,70.55555555555556,71.25,71.31034482758619,71.33333333333336,71.93548387096776,71.75,71.87878787878788,72.20588235294119,72.3714285714286,72.75,73.27027027027025,73.6578947368421,73.56410256410255,73.64999999999999,73.29268292682926,73.45238095238096,73.69767441860463,73.8181818181818,74.20000000000002,74.3913043478261,74.76595744680849,74.79166666666666,74.93877551020408,75.12,75.50980392156863,75.90384615384617,76.24528301886791,76.3888888888889,76.65454545454544,77.07142857142857,77.29824561403508,77.5,77.57627118644066,77.81666666666665,77.68852459016395,77.64516129032258,77.7777777777778,78.0625,78.26153846153848,78.24242424242425,78.4179104477612,78.61764705882352,78.8985507246377,79.02857142857144,79.30985915492955,79.52777777777779,79.6027397260274,79.85135135135135,80.12,80.38157894736842,80.61038961038959,80.85897435897435,81.10126582278482,81.29999999999998,81.53086419753085,81.7560975609756,81.97590361445783,82.19047619047618,82.39999999999999,82.60465116279069,82.80459770114943,83.0,83.19101123595507,83.35555555555557,83.53846153846153,83.68478260869564,83.66666666666666,83.6765336765337], marker='o', color='#0bf933', markerfacecolor='None',markeredgecolor='#0bf933', markeredgewidth=0.8)
plt.plot(x, [100.0,98.0,98.66666666666666,99.0,98.79999999999998,98.66666666666666,97.2857142857143,85.125,78.0,74.60000000000001,72.09090909090911,72.66666666666666,71.07692307692308,70.64285714285712,69.2,67.875,66.76470588235294,66.3888888888889,65.89473684210525,66.35000000000001,67.09523809523809,67.95454545454547,68.69565217391303,68.79166666666664,69.48,69.19230769230771,69.2222222222222,69.71428571428574,69.72413793103446,69.33333333333336,70.0,69.71875,69.75757575757576,69.8529411764706,70.14285714285712,70.58333333333334,71.0,71.36842105263158,71.28205128205128,71.27499999999999,70.60975609756098,70.69047619047618,70.53488372093022,70.72727272727273,70.95555555555555,70.93478260869564,71.10638297872342,71.04166666666666,70.85714285714286,70.67999999999998,71.15686274509802,71.63461538461537,72.05660377358491,72.27777777777779,72.61818181818181,73.10714285714288,73.40350877192984,73.67241379310347,73.81355932203391,74.11666666666666,74.04918032786885,74.06451612903224,74.25396825396824,74.59375,74.84615384615384,74.87878787878788,75.1044776119403,75.3529411764706,75.68115942028986,75.85714285714288,76.1830985915493,76.3888888888889,76.4794520547945,76.79729729729729,77.08000000000001,77.38157894736842,77.64935064935067,77.93589743589745,78.21518987341774,78.45000000000002,78.71604938271605,78.95121951219514,79.20481927710843,79.45238095238095,79.69411764705885,79.93023255813954,80.16091954022988,80.38636363636364,80.6067415730337,80.8,81.010989010989,81.18478260869564,81.19354838709678,81.22050622050621], marker='o', color='#7fa1ea', markerfacecolor='None',markeredgecolor='#7fa1ea', markeredgewidth=0.8)
plt.plot(x, [100.0,98.0,98.66666666666666,99.0,98.79999999999998,98.66666666666666,97.2857142857143,85.125,78.0,74.60000000000001,70.90909090909089,70.41666666666666,68.0,66.42857142857143,64.73333333333333,63.249999999999986,62.0,61.55555555555556,60.0,60.0,58.380952380952394,56.95454545454546,56.21739130434783,55.83333333333333,55.60000000000001,53.46153846153847,51.55555555555556,50.67857142857144,52.37931034482757,53.966666666666654,55.45161290322581,56.65625,56.96969696969698,58.02941176470587,57.94285714285714,57.91666666666667,57.81081081081082,58.289473684210535,58.02564102564103,59.075,59.829268292682926,60.28571428571429,61.16279069767442,61.18181818181817,61.31111111111112,62.02173913043477,61.93617021276596,62.22916666666667,62.6734693877551,63.260000000000005,63.72549019607844,64.34615384615383,64.90566037735847,65.14814814814814,65.52727272727272,66.10714285714286,66.29824561403508,66.60344827586208,66.72881355932203,66.96666666666668,66.85245901639345,66.77419354838709,66.79365079365081,66.96875,66.92307692307692,66.89393939393939,66.8955223880597,67.08823529411767,67.53623188405798,67.51428571428572,67.7887323943662,68.05555555555556,68.05479452054794,68.48648648648647,68.88,69.28947368421052,69.6883116883117,70.07692307692308,70.45569620253163,70.82500000000002,71.1851851851852,71.53658536585364,71.87951807228914,72.21428571428574,72.54117647058821,72.86046511627909,73.17241379310347,73.40909090909089,73.64044943820225,73.93333333333331,74.20879120879123,74.48913043478261,74.41935483870965,74.43157443157442], marker='o', color='#ff0000', markerfacecolor='None',markeredgecolor='#ff0000', markeredgewidth=0.8)
plt.plot(x, [100.0,98.0,98.66666666666666,99.0,98.79999999999998,98.66666666666666,97.2857142857143,85.125,78.0,74.60000000000001,72.09090909090911,72.83333333333336,71.15384615384617,70.5,69.2,67.875,66.7058823529412,66.3888888888889,65.78947368421053,66.14999999999999,67.14285714285712,68.0,68.86956521739128,68.91666666666666,69.64,69.73076923076924,70.33333333333336,70.9642857142857,70.9655172413793,70.83333333333336,71.45161290322582,71.09375,71.12121212121212,71.5,71.74285714285715,72.19444444444446,72.56756756756758,72.94736842105262,72.87179487179489,72.875,72.53658536585364,72.7142857142857,72.69767441860463,72.79545454545453,73.02222222222223,73.13043478260872,73.29787234042554,73.3125,73.2857142857143,73.22000000000001,73.6470588235294,74.07692307692308,74.45283018867926,74.62962962962965,74.92727272727275,75.375,75.63157894736842,75.86206896551722,75.96610169491524,76.23333333333333,76.13114754098362,76.11290322580645,76.26984126984125,76.578125,76.79999999999998,76.8030303030303,77.0,77.22058823529413,77.52173913043477,77.67142857142856,77.9718309859155,78.20833333333334,78.30136986301372,78.56756756756758,78.85333333333334,79.13157894736842,79.37662337662337,79.64102564102564,79.89873417721518,80.11249999999998,80.35802469135801,80.59756097560977,80.83132530120483,81.0357142857143,81.25882352941176,81.47674418604652,81.68965517241381,81.89772727272727,82.10112359550564,82.2777777777778,82.47252747252746,82.63043478260872,82.63440860215053,82.64693264693265], marker='o', color='#000000', markerfacecolor='None',markeredgecolor='#000000', markeredgewidth=0.8)
plt.plot(x, [100.0,98.0,98.66666666666666,99.0,98.79999999999998,98.66666666666666,97.2857142857143,85.125,78.0,74.60000000000001,71.54545454545453,71.25,69.30769230769229,68.07142857142857,66.60000000000001,65.25,63.88235294117648,63.66666666666667,62.526315789473685,62.3,61.0,60.36363636363636,60.39130434782611,60.583333333333336,60.480000000000004,59.11538461538463,57.92592592592591,57.892857142857146,58.655172413793096,59.0,59.54838709677419,60.25,60.57575757575758,61.411764705882355,61.62857142857142,61.972222222222214,62.02702702702702,62.23684210526316,62.1025641025641,62.7,63.26829268292683,63.76190476190477,64.39534883720931,64.54545454545453,64.79999999999998,65.3913043478261,65.61702127659576,65.70833333333334,66.0,66.48,66.78431372549018,67.19230769230771,67.47169811320757,67.5185185185185,67.96363636363637,68.5,68.75438596491226,68.96551724137932,69.01694915254235,69.33333333333336,69.34426229508198,69.33870967741937,69.44444444444444,69.796875,69.95384615384616,70.06060606060605,70.23880597014927,70.38235294117648,70.75362318840578,70.74285714285715,70.943661971831,71.2222222222222,71.21917808219177,71.58108108108107,71.96000000000002,72.32894736842105,72.6103896103896,72.96153846153847,73.30379746835443,73.51250000000002,73.8148148148148,74.13414634146342,74.42168674698793,74.65476190476191,74.92941176470586,75.22093023255812,75.50574712643677,75.6818181818182,75.8876404494382,76.08888888888887,76.35164835164835,76.56521739130436,76.50537634408602,76.52295152295152], marker='o', color='#ffcc66', markerfacecolor='None',markeredgecolor='#ffcc66', markeredgewidth=0.8)
plt.legend(['NB', 'Chi-Squared', 'FCBF', 'EFS', 'IG', 'OFS'], fontsize='small', shadow=True, fancybox=True)
plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Accuracy (%)', fontsize=12)
np.arange(100, 10500, step=1000)
plt.yticks(np.arange(0, 120, step=20))
plt.tight_layout()
plt.savefig('acc_spam_assassin_10.eps')