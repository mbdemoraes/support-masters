import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-darkgrid')
x = np.arange(100, 6100, 100)
plt.plot(x, [53.0,60.5,67.0,69.25,70.2,72.33333333333336,73.14285714285712,73.625,74.55555555555556,75.10000000000001,76.45454545454547,76.66666666666666,76.61538461538463,77.14285714285714,78.0,78.6875,78.76470588235294,79.33333333333334,79.78947368421052,80.14999999999999,80.3809523809524,80.77272727272727,81.08695652173913,81.25,81.55999999999999,81.88461538461537,82.03703703703705,82.25,82.48275862068965,82.66666666666666,82.51612903225806,82.5,82.63636363636364,82.76470588235294,82.85714285714288,83.05555555555556,83.05405405405405,83.10526315789475,83.20512820512819,83.29999999999998,83.48780487804878,83.6190476190476,83.72093023255816,83.8181818181818,83.95555555555555,83.76086956521739,83.82978723404256,83.83333333333336,83.85714285714286,83.98,84.01960784313725,84.07692307692308,84.1698113207547,84.29629629629629,84.32727272727274,84.44642857142857,84.49122807017544,84.51724137931035,84.54237288135594,84.60383653044205], marker='o', color='#996600', markerfacecolor='None',markeredgecolor='#996600', markeredgewidth=0.8)
plt.plot(x, [53.0,60.5,67.0,69.25,70.2,72.5,74.0,74.75,75.22222222222221,75.89999999999999,76.27272727272727,76.91666666666666,77.53846153846153,77.78571428571426,78.79999999999998,78.875,79.11764705882352,79.44444444444444,79.89473684210525,80.14999999999999,80.42857142857143,80.68181818181816,81.08695652173913,81.41666666666666,81.60000000000001,81.84615384615383,82.07407407407409,82.35714285714288,82.55172413793103,82.7,82.06451612903224,81.84375,81.42424242424241,81.32352941176472,81.14285714285712,80.75,80.67567567567566,80.52631578947367,80.20512820512819,80.0,79.95121951219514,79.83333333333334,79.74418604651164,79.61363636363636,79.55555555555556,79.39130434782611,79.19148936170212,78.9375,78.57142857142857,78.38000000000001,78.17647058823528,77.98076923076924,77.77358490566039,77.6111111111111,77.47272727272728,77.2857142857143,77.12280701754388,77.0,76.81355932203391,76.71392827356132], marker='o', color='#0bf933', markerfacecolor='None',markeredgecolor='#0bf933', markeredgewidth=0.8)
plt.plot(x, [53.0,60.5,67.0,69.25,70.2,72.0,73.57142857142857,75.125,75.66666666666666,76.0,76.54545454545453,77.41666666666666,78.07692307692308,78.57142857142857,79.39999999999999,79.5,79.76470588235294,80.05555555555556,80.63157894736842,80.95000000000002,81.19047619047618,81.45454545454547,81.82608695652173,82.08333333333334,82.36,82.46153846153847,82.7037037037037,82.9642857142857,83.17241379310346,83.33333333333336,82.64516129032258,82.4375,82.06060606060605,81.91176470588233,81.57142857142857,81.2222222222222,81.08108108108107,80.97368421052633,80.76923076923076,80.52499999999999,80.41463414634146,80.26190476190477,80.1627906976744,80.0,79.93333333333335,79.76086956521739,79.5531914893617,79.27083333333334,78.89795918367348,78.72000000000001,78.50980392156863,78.28846153846155,78.0,77.79629629629629,77.65454545454544,77.42857142857143,77.28070175438596,77.13793103448276,76.93220338983052,76.86405337781483], marker='o', color='#7fa1ea', markerfacecolor='None',markeredgecolor='#7fa1ea', markeredgewidth=0.8)
plt.plot(x, [53.0,60.5,67.0,69.25,70.2,67.33333333333334,65.14285714285714,63.625,62.1111111111111,61.2,60.18181818181817,59.416666666666664,58.92307692307692,58.5,58.06666666666665,57.75,57.52941176470587,57.222222222222214,56.94736842105264,56.75,56.42857142857143,56.13636363636364,55.913043478260875,55.70833333333333,55.480000000000004,55.30769230769231,55.14814814814814,55.000000000000014,54.79310344827586,54.63333333333334,54.58064516129032,54.46875,54.36363636363636,54.294117647058826,54.28571428571429,54.19444444444444,54.135135135135144,54.026315789473685,53.8974358974359,53.825,53.73170731707317,53.66666666666667,53.46511627906976,53.11363636363636,52.8,52.6304347826087,52.48936170212765,52.4375,52.38775510204083,52.32000000000001,52.294117647058826,52.32692307692308,52.283018867924525,52.25925925925925,52.236363636363635,52.19642857142857,52.12280701754388,52.12068965517243,52.11864406779661,52.1768140116764], marker='o', color='#ff0000', markerfacecolor='None',markeredgecolor='#ff0000', markeredgewidth=0.8)
plt.plot(x, [53.0,60.5,67.0,69.25,70.2,72.16666666666666,73.57142857142857,75.0,75.66666666666666,76.0,76.54545454545453,77.33333333333334,78.0,78.5,79.33333333333334,79.4375,79.7058823529412,80.0,80.57894736842105,80.89999999999999,81.19047619047618,81.40909090909089,81.78260869565216,82.04166666666666,82.32000000000002,82.42307692307692,82.66666666666666,82.92857142857143,83.13793103448278,83.29999999999998,82.58064516129033,82.28125,81.90909090909089,81.76470588235294,81.39999999999999,81.05555555555556,80.89189189189189,80.81578947368419,80.5897435897436,80.375,80.26829268292683,80.09523809523809,80.02325581395348,79.86363636363636,79.8,79.6304347826087,79.42553191489364,79.14583333333336,78.77551020408164,78.60000000000001,78.41176470588233,78.19230769230771,77.90566037735847,77.70370370370371,77.56363636363635,77.3392857142857,77.17543859649122,77.0344827586207,76.83050847457628,76.76396997497913], marker='o', color='#000000', markerfacecolor='None',markeredgecolor='#000000', markeredgewidth=0.8)
plt.plot(x, [53.0,60.5,67.0,69.25,70.2,69.16666666666666,67.28571428571426,66.875,66.44444444444444,64.79999999999998,64.1818181818182,63.33333333333333,62.846153846153854,62.142857142857146,61.39999999999999,61.0625,60.23529411764706,59.94444444444444,59.526315789473685,58.95,58.857142857142854,58.909090909090914,58.95652173913042,58.416666666666664,58.27999999999999,57.999999999999986,58.07407407407409,58.107142857142854,58.55172413793103,58.36666666666666,58.38709677419355,58.25,58.09090909090911,58.26470588235294,58.37142857142858,58.333333333333336,58.24324324324324,58.342105263157904,58.17948717948717,58.075,58.07317073170732,58.04761904761905,58.11627906976743,58.15909090909089,58.2,58.152173913043484,58.1276595744681,58.062499999999986,58.28571428571429,58.32000000000001,58.3921568627451,58.34615384615385,58.415094339622655,58.42592592592591,58.36363636363636,58.357142857142854,58.368421052631575,58.41379310344827,58.42372881355932,58.43202668890741], marker='o', color='#ffcc66', markerfacecolor='None',markeredgecolor='#ffcc66', markeredgewidth=0.8)
plt.legend(['NB', 'Chi-Squared', 'FCBF', 'EFS', 'IG', 'OFS'], fontsize='small', shadow=True, fancybox=True)
plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Accuracy (%)', fontsize=12)
np.arange(100, 7100, step=1000)
plt.yticks(np.arange(0, 120, step=20))
plt.tight_layout()
plt.savefig('acc_mailing_list_100.eps')