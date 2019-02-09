import matplotlib.pyplot as plt
import numpy as np

x = np.arange(100, 10100, 100)

plt.gca().set_color_cycle(['blue'])

plt.plot(x, [35.0,27.500000000000007,30.0,29.75,28.999999999999993,29.833333333333336,29.714285714285715,29.625,29.55555555555555,29.9,29.454545454545457,29.166666666666668,30.0,30.428571428571427,30.06666666666667,30.1875,29.764705882352935,29.611111111111107,29.578947368421048,29.449999999999996,28.952380952380956,29.272727272727273,29.304347826086957,29.375,29.360000000000007,29.46153846153846,29.40740740740741,29.321428571428562,29.241379310344833,29.199999999999996,29.419354838709676,29.531249999999993,29.757575757575758,29.470588235294123,29.714285714285715,29.916666666666668,29.810810810810814,29.684210526315788,29.641025641025642,29.925000000000004,29.926829268292686,29.928571428571427,30.02325581395349,29.954545454545457,30.0,29.84782608695652,29.744680851063833,29.770833333333336,29.591836734693878,29.6,29.843137254901954,29.96153846153846,30.245283018867916,30.5,30.636363636363633,30.892857142857146,30.982456140350884,31.12068965517242,31.355932203389834,31.550000000000004,31.639344262295083,31.758064516129032,32.03174603174603,32.234375,32.35384615384616,32.5909090909091,32.62686567164179,32.764705882352935,32.869565217391305,33.028571428571425,33.0281690140845,33.26388888888889,33.424657534246585,33.567567567567565,33.60000000000001,33.75,33.870129870129865,33.987179487179496,33.9873417721519,34.10000000000001,34.25925925925925,34.40243902439023,34.6144578313253,34.67857142857144,34.87058823529412,35.0,34.977011494252885,35.045454545454554,35.12359550561798,35.33333333333333,35.42857142857143,35.54347826086956,35.612903225806456,35.64893617021277,35.736842105263165,35.66666666666668,35.63917525773196,35.76530612244898,35.75757575757576,35.88
], marker="o", color='#996600', markerfacecolor="None",
         markeredgecolor='#996600', markeredgewidth=0.8)
#plt.plot(x, [35.0,56.999999999999986,59.333333333333336,62.250000000000014,64.39999999999999,64.83333333333334,65.7142857142857,66.375,66.8888888888889,66.89999999999999,67.63636363636364,68.16666666666664,67.53846153846153,67.28571428571426,67.8,67.8125,68.3529411764706,68.6111111111111,68.73684210526315,68.95000000000002,69.52380952380952,69.27272727272727,69.30434782608697,69.29166666666664,69.36,69.30769230769229,69.4074074074074,69.5357142857143,69.65517241379311,69.73333333333333,69.54838709677418,69.46875,69.27272727272727,69.58823529411767,69.37142857142858,69.19444444444444,69.32432432432434,69.47368421052633,69.53846153846153,69.27499999999999,69.29268292682924,69.30952380952382,69.23255813953487,69.31818181818184,69.28888888888889,69.45652173913045,69.57446808510636,69.5625,69.75510204081634,69.76,69.52941176470587,69.42307692307692,69.15094339622642,68.9074074074074,68.78181818181817,68.5357142857143,68.45614035087718,68.32758620689654,68.10169491525424,67.91666666666666,67.83606557377048,67.72580645161291,67.33333333333334,66.984375,66.56923076923077,66.28787878787877,65.82089552238804,65.47058823529413,65.10144927536234,64.79999999999998,64.35211267605634,64.1527777777778,63.89041095890411,63.62162162162163,63.25333333333333,63.013157894736835,62.753246753246756,62.5,62.1392405063291,61.89999999999999,61.71604938271605,61.52439024390243,61.40963855421687,61.15476190476191,61.03529411764704,60.86046511627909,60.54022988505746,60.3181818181818,60.112359550561806,60.044444444444444,59.86813186813187,59.71739130434783,59.5268817204301,59.308510638297875,59.231578947368426,58.97916666666667,58.742268041237125,58.61224489795917,58.42424242424242,58.330000000000005
#], marker="o", color='#0bf933', markerfacecolor="None",
#         markeredgecolor='#0bf933', markeredgewidth=0.8)
#plt.plot(x, [35.0,55.000000000000014,57.666666666666664,60.750000000000014,63.39999999999999,63.83333333333333,64.85714285714288,65.625,66.22222222222221,66.29999999999998,67.09090909090911,67.66666666666664,67.07692307692308,66.85714285714288,67.39999999999999,67.4375,68.0,68.2777777777778,68.42105263157895,68.64999999999999,69.23809523809523,69.0,69.04347826086955,69.04166666666666,69.12,69.07692307692308,69.18518518518519,69.32142857142857,69.44827586206897,69.53333333333332,69.35483870967742,69.28125,69.09090909090911,69.41176470588233,69.2,69.02777777777779,69.16216216216218,69.31578947368419,69.38461538461537,69.125,69.14634146341463,69.16666666666666,69.09302325581395,69.18181818181816,69.15555555555557,69.32608695652173,69.44680851063832,69.4375,69.63265306122447,69.64,69.41176470588233,69.30769230769229,69.0377358490566,68.7962962962963,68.67272727272726,68.42857142857143,68.35087719298245,68.22413793103446,68.0,67.81666666666665,67.31147540983605,67.20967741935486,66.92063492063492,66.578125,66.16923076923078,65.89393939393939,65.43283582089553,65.08823529411767,64.72463768115941,64.42857142857143,63.985915492957744,63.79166666666667,63.534246575342465,63.28378378378379,62.94666666666667,62.710526315789465,62.44155844155843,62.19230769230769,61.82278481012658,61.5625,61.382716049382715,61.19512195121952,61.084337349397586,60.880952380952394,60.635294117647064,60.48837209302326,60.21839080459769,60.03409090909089,59.91011235955055,59.86666666666666,59.76923076923076,59.641304347826086,59.50537634408603,59.29787234042554,59.13684210526317,58.833333333333336,58.659793814433,58.530612244897966,58.32323232323232,58.209999999999994
#], marker="o", color='#7fa1ea', markerfacecolor="None",
#         markeredgecolor='#7fa1ea', markeredgewidth=0.8)
plt.plot(x, [35.0,57.499999999999986,60.0,62.749999999999986,65.0,65.16666666666664,66.0,66.625,67.1111111111111,67.10000000000001,67.81818181818184,68.33333333333334,67.69230769230771,67.42857142857143,67.93333333333335,67.9375,68.47058823529413,68.7222222222222,68.8421052631579,69.04999999999998,69.6190476190476,69.36363636363636,69.39130434782611,69.375,69.44000000000001,69.38461538461537,69.4814814814815,69.60714285714288,69.72413793103446,69.79999999999998,69.61290322580645,69.53125,69.33333333333336,69.6470588235294,69.42857142857143,69.25,69.37837837837837,69.52631578947367,69.5897435897436,69.32500000000002,69.34146341463416,69.35714285714288,69.27906976744184,69.36363636363636,69.33333333333336,69.5,69.61702127659576,69.60416666666666,69.79591836734696,69.77999999999999,69.23529411764706,68.59615384615384,68.15094339622642,67.7037037037037,67.16363636363634,66.76785714285712,66.22807017543859,65.75862068965516,65.40677966101693,65.03333333333332,64.5737704918033,64.16129032258063,63.920634920634924,63.625,63.24615384615383,63.015151515151516,62.61194029850746,62.308823529411754,61.9855072463768,61.75714285714285,61.352112676056336,61.18055555555556,60.95890410958906,60.729729729729726,60.41333333333331,60.197368421052616,59.98701298701299,59.74358974358974,59.44303797468355,59.22500000000001,59.08641975308642,58.92682926829268,58.83132530120482,58.59523809523809,58.47058823529413,58.337209302325576,58.06896551724138,57.90909090909089,57.74157303370786,57.7,57.549450549450555,57.423913043478265,57.25806451612904,57.06382978723404,56.92631578947369,56.63541666666667,56.39175257731959,56.30612244897959,56.09090909090911,56.010000000000005
], marker="o", color='#ff0000', markerfacecolor="None",
         markeredgecolor='#ff0000', markeredgewidth=0.8)
#plt.plot(x, [35.0,55.000000000000014,58.333333333333336,61.5,64.0,64.33333333333334,65.28571428571426,66.0,66.55555555555556,66.60000000000001,67.36363636363636,67.91666666666666,67.30769230769229,67.07142857142857,67.60000000000001,67.625,68.17647058823528,68.44444444444444,68.57894736842105,68.79999999999998,69.3809523809524,69.13636363636364,69.17391304347827,69.16666666666666,69.24,69.19230769230771,69.2962962962963,69.42857142857143,69.55172413793103,69.63333333333334,69.45161290322582,69.375,69.18181818181816,69.5,69.28571428571426,69.1111111111111,69.24324324324324,69.39473684210525,69.46153846153847,69.2,69.21951219512196,69.23809523809523,69.1627906976744,69.25,69.2222222222222,69.39130434782611,69.51063829787233,69.5,69.69387755102039,69.7,69.47058823529413,69.36538461538463,69.09433962264153,68.85185185185185,68.72727272727273,68.48214285714288,68.40350877192984,68.27586206896554,68.05084745762711,67.86666666666666,67.78688524590164,67.67741935483869,67.33333333333334,66.984375,66.56923076923077,66.28787878787877,65.82089552238804,65.47058823529413,65.10144927536234,64.79999999999998,64.35211267605634,64.1527777777778,63.89041095890411,63.62162162162163,63.25333333333333,63.013157894736835,62.753246753246756,62.5,62.1392405063291,61.89999999999999,61.71604938271605,61.52439024390243,61.40963855421687,61.15476190476191,61.03529411764704,60.86046511627909,60.54022988505746,60.3181818181818,60.112359550561806,60.044444444444444,59.86813186813187,59.71739130434783,59.5268817204301,59.308510638297875,59.14736842105263,58.895833333333336,58.70103092783505,58.642857142857125,58.484848484848484,58.47000000000001
#], marker="o", color='#000000', markerfacecolor="None",
#         markeredgecolor='#000000', markeredgewidth=0.8)
plt.plot(x, [35.0,57.499999999999986,60.0,62.749999999999986,65.0,65.16666666666664,66.0,66.625,67.1111111111111,67.10000000000001,67.81818181818184,68.33333333333334,67.69230769230771,67.42857142857143,67.93333333333335,67.9375,68.47058823529413,68.7222222222222,68.8421052631579,69.04999999999998,69.6190476190476,69.36363636363636,69.39130434782611,69.375,69.44000000000001,69.38461538461537,69.4814814814815,69.60714285714288,69.72413793103446,69.79999999999998,69.61290322580645,69.53125,69.33333333333336,69.6470588235294,69.42857142857143,69.25,69.37837837837837,69.52631578947367,69.5897435897436,69.32500000000002,69.34146341463416,69.35714285714288,69.27906976744184,69.36363636363636,69.33333333333336,69.5,69.61702127659576,69.60416666666666,69.79591836734696,69.77999999999999,69.23529411764706,68.59615384615384,68.15094339622642,67.7037037037037,67.16363636363634,66.76785714285712,66.21052631578948,65.74137931034484,65.38983050847457,65.01666666666667,64.55737704918033,64.12903225806451,63.8888888888889,63.593750000000014,63.26153846153845,63.04545454545455,62.64179104477613,62.36764705882352,62.04347826086958,61.8,61.38028169014085,61.2361111111111,61.01369863013698,60.79729729729729,60.50666666666666,60.315789473684205,60.09090909090911,59.8974358974359,59.56962025316456,59.3625,59.19753086419753,59.03658536585364,58.927710843373475,58.72619047619047,58.647058823529406,58.53488372093024,58.287356321839084,58.147727272727266,57.96629213483148,57.92222222222222,57.76923076923076,57.6304347826087,57.4731182795699,57.31914893617021,57.16842105263159,56.90625,56.69072164948453,56.632653061224474,56.474747474747474,56.39999999999999
], marker="o", color='#ffcc66', markerfacecolor="None",
         markeredgecolor='#ffcc66', markeredgewidth=0.8)


#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper le0t')
#plt.legend(['NB', 'Chi-Squared', 'FCBF', 'EFS', 'IG', 'OFS'], loc='‘lower right', fontsize='small', shadow=True, fancybox=True)
plt.legend(['NB', 'EFS', 'OFS'], loc='‘lower right', fontsize='small', shadow=True, fancybox=True)

plt.axvline(x=5000, ymax=1, color='#a1a1ee', linewidth=0.8)

plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Accuracy (%)', fontsize=12)

#plt.grid(color='k', linestyle='-.', linewidth=0.4)
plt.xticks(np.arange(100, 11100, step=1000))
plt.yticks(np.arange(40, 110, step=10))

plt.tight_layout()

#plt.show()
plt.savefig('acc_sudden_10.eps')