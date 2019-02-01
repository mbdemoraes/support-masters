import matplotlib.pyplot as plt
import numpy as np

x = np.arange(100, 6100, 100)

plt.gca().set_color_cycle(['blue'])

plt.plot(x, [53.0,60.5,67.0,69.25,70.2,72.33333333333336,73.14285714285712,73.625,74.55555555555556,75.10000000000001,76.45454545454547,76.66666666666666,76.61538461538463,77.14285714285714,78.0,78.6875,78.76470588235294,79.33333333333334,79.78947368421052,80.14999999999999,80.3809523809524,80.77272727272727,81.08695652173913,81.25,81.55999999999999,81.88461538461537,82.03703703703705,82.25,82.48275862068965,82.66666666666666,82.51612903225806,82.5,82.63636363636364,82.76470588235294,82.85714285714288,83.05555555555556,83.05405405405405,83.10526315789475,83.20512820512819,83.29999999999998,83.48780487804878,83.6190476190476,83.72093023255816,83.8181818181818,83.95555555555555,83.76086956521739,83.82978723404256,83.83333333333336,83.85714285714286,83.98,84.01960784313725,84.07692307692308,84.1698113207547,84.29629629629629,84.32727272727274,84.44642857142857,84.49122807017544,84.51724137931035,84.54237288135594,84.60383653044205
], marker="o", color='#996600', markerfacecolor="None",
         markeredgecolor='#996600', markeredgewidth=0.8)
plt.plot(x, [53.0,56.999999999999986,62.66666666666667,63.0,65.20000000000002,66.5,66.57142857142857,67.125,66.8888888888889,67.70000000000002,68.0,69.0,69.30769230769229,69.14285714285712,70.0,70.1875,70.23529411764706,70.27777777777779,70.42105263157895,70.79999999999998,71.19047619047618,71.59090909090911,71.8695652173913,71.91666666666664,72.15999999999998,72.23076923076924,72.44444444444444,72.60714285714288,72.93103448275862,72.93333333333331,72.61290322580645,72.53125,72.51515151515152,72.44117647058825,72.3142857142857,72.2222222222222,72.21621621621622,72.28947368421052,72.17948717948718,72.20000000000002,72.0,71.8809523809524,71.79069767441861,71.75,71.73333333333333,71.58695652173913,71.46808510638299,71.25,70.89795918367348,70.76,70.52941176470587,70.42307692307692,70.1698113207547,69.94444444444444,69.79999999999998,69.69642857142857,69.52631578947367,69.37931034482757,69.22033898305085,69.1909924937448
], marker="o", color='#0bf933', markerfacecolor="None",
         markeredgecolor='#0bf933', markeredgewidth=0.8)
plt.plot(x, [53.0,59.5,61.33333333333333,64.0,66.0,67.0,67.28571428571426,67.625,67.55555555555556,68.20000000000002,68.63636363636364,69.75,69.84615384615383,69.57142857142857,69.86666666666666,69.875,70.17647058823528,70.2222222222222,70.36842105263158,70.75,71.04761904761905,71.18181818181816,71.43478260869564,71.375,71.52,71.65384615384617,71.8888888888889,72.14285714285712,72.55172413793105,72.56666666666665,72.29032258064515,72.1875,72.09090909090911,72.02941176470587,71.91428571428573,71.83333333333336,71.83783783783782,71.89473684210525,71.79487179487181,71.82500000000002,71.6341463414634,71.52380952380952,71.44186046511628,71.40909090909089,71.39999999999999,71.26086956521739,71.14893617021276,70.9375,70.59183673469387,70.46000000000001,70.23529411764706,70.13461538461537,69.88679245283018,69.66666666666666,69.50909090909092,69.39285714285712,69.24561403508774,69.08620689655173,68.93220338983052,68.95746455379482
], marker="o", color='#7fa1ea', markerfacecolor="None",
         markeredgecolor='#7fa1ea', markeredgewidth=0.8)
plt.plot(x, [53.0,49.5,50.0,50.24999999999999,45.199999999999996,46.0,46.57142857142856,47.125,47.44444444444445,47.699999999999996,47.9090909090909,48.08333333333333,48.23076923076923,48.35714285714287,48.466666666666676,48.5625,48.647058823529406,48.72222222222222,48.78947368421053,48.85000000000001,48.90476190476191,48.954545454545446,49.0,48.91666666666668,48.959999999999994,49.0,49.037037037037045,49.07142857142856,49.13793103448275,49.16666666666667,49.0,49.03125,48.545454545454554,48.58823529411766,47.68571428571429,46.83333333333333,46.91891891891891,47.0,46.28205128205128,46.375,46.46341463414635,46.547619047619044,46.62790697674418,46.704545454545446,46.77777777777778,46.847826086956516,46.893617021276604,46.95833333333333,47.04081632653061,46.56,46.627450980392155,46.71153846153846,46.622641509433954,46.685185185185176,46.727272727272734,46.5,46.57894736842105,46.06896551724139,45.559322033898304,45.62135112593829
], marker="o", color='#ff0000', markerfacecolor="None",
         markeredgecolor='#ff0000', markeredgewidth=0.8)
plt.plot(x, [53.0,56.499999999999986,61.66666666666667,63.0,65.20000000000002,66.33333333333334,66.7142857142857,67.25,67.0,67.89999999999999,68.36363636363636,69.5,69.69230769230771,69.5,69.93333333333335,70.125,70.41176470588233,70.44444444444444,70.57894736842105,70.95000000000002,71.23809523809523,71.36363636363636,71.6086956521739,71.66666666666666,71.91999999999999,72.03846153846155,72.33333333333336,72.57142857142857,72.9655172413793,72.96666666666668,72.67741935483873,72.5625,72.45454545454547,72.38235294117648,72.25714285714285,72.16666666666666,72.16216216216218,72.21052631578947,72.1025641025641,72.125,71.92682926829266,71.80952380952382,71.72093023255816,71.6818181818182,71.66666666666666,71.52173913043477,71.40425531914892,71.1875,70.83673469387756,70.70000000000002,70.47058823529413,70.36538461538463,70.11320754716982,69.8888888888889,69.72727272727273,69.60714285714288,69.45614035087718,69.29310344827584,69.13559322033898,69.12427022518764
], marker="o", color='#000000', markerfacecolor="None",
         markeredgecolor='#000000', markeredgewidth=0.8)
plt.plot(x, [53.0,48.0,47.33333333333333,50.24999999999999,50.199999999999996,49.66666666666667,50.285714285714285,49.75,50.0,50.5,51.45454545454545,51.33333333333333,51.0,50.57142857142856,50.733333333333334,50.81250000000001,50.94117647058823,51.05555555555555,50.89473684210526,50.85,51.1904761904762,51.59090909090908,51.826086956521735,51.749999999999986,51.64,51.61538461538463,51.814814814814824,51.71428571428571,52.0,51.8,52.29032258064517,52.531249999999986,52.60606060606061,52.82352941176471,52.885714285714286,53.08333333333333,53.10810810810811,53.236842105263165,53.128205128205124,53.3,53.36585365853658,53.40476190476191,53.51162790697674,53.56818181818181,53.42222222222223,53.39130434782608,53.36170212765957,53.29166666666667,53.42857142857143,53.519999999999996,53.72549019607844,53.75,53.867924528301884,53.94444444444444,54.036363636363646,54.017857142857125,54.105263157894726,54.0344827586207,54.08474576271186,54.02835696413679
], marker="o", color='#ffcc66', markerfacecolor="None",
         markeredgecolor='#ffcc66', markeredgewidth=0.8)


#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper le0t')
plt.legend(['NB', 'Chi-Squared', 'FCBF', 'EFS', 'IG', 'OFS'], loc='‘lower right', fontsize='small', shadow=True, fancybox=True)


plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Accuracy (%)', fontsize=12)

#plt.grid(color='k', linestyle='-.', linewidth=0.4)
plt.xticks(np.arange(100, 7100, step=1000))
plt.yticks(np.arange(40, 110, step=10))

plt.tight_layout()

#plt.show()
plt.savefig('acc_mailing_list_10.png')
