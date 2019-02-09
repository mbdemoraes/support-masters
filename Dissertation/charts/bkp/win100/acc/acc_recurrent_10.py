import matplotlib.pyplot as plt
import numpy as np

x = np.arange(100, 10100, 100)

plt.gca().set_color_cycle(['blue'])

plt.plot(x, [33.0,41.5,38.66666666666667,38.0,37.39999999999999,36.33333333333333,35.85714285714287,36.875,36.33333333333333,37.300000000000004,37.272727272727266,36.83333333333333,37.38461538461537,37.14285714285715,37.13333333333333,37.625,37.294117647058826,37.44444444444445,37.57894736842105,37.5,37.523809523809526,38.31818181818182,38.17391304347826,38.41666666666667,38.76,38.807692307692314,38.8888888888889,39.285714285714285,39.31034482758621,39.699999999999996,39.87096774193548,39.875,40.15151515151514,40.1764705882353,40.37142857142857,40.66666666666667,40.72972972972973,40.81578947368421,41.05128205128205,41.02499999999999,41.02439024390243,41.047619047619044,41.186046511627914,41.34090909090908,41.31111111111112,41.32608695652174,41.42553191489362,41.33333333333333,41.55102040816326,41.63999999999999,41.431372549019606,41.403846153846146,41.16981132075472,40.925925925925924,40.74545454545454,40.55357142857144,40.29824561403508,40.172413793103445,40.01694915254238,39.966666666666676,39.885245901639344,39.661290322580655,39.55555555555555,39.46875,39.36923076923076,39.272727272727266,39.08955223880598,38.91176470588234,38.753623188405804,38.61428571428571,38.45070422535212,38.34722222222222,38.21917808219178,38.135135135135144,37.98666666666667,37.82894736842105,37.84415584415586,37.7051282051282,37.68354430379747,37.625,37.641975308641975,37.82926829268292,37.78313253012049,37.86904761904761,37.96470588235293,38.01162790697674,38.03448275862069,38.1590909090909,38.19101123595505,38.322222222222216,38.40659340659341,38.42391304347826,38.53763440860216,38.57446808510638,38.66315789473685,38.77083333333332,38.83505154639175,38.87755102040817,38.97979797979798,39.0
], marker="o", color='#996600', markerfacecolor="None",
         markeredgecolor='#996600', markeredgewidth=0.8)
#plt.plot(x, [33.0,40.5,48.0,51.249999999999986,54.0,56.16666666666667,57.142857142857125,56.999999999999986,58.222222222222214,57.89999999999999,58.45454545454546,59.166666666666664,58.92307692307692,59.42857142857143,59.60000000000001,59.3125,59.82352941176471,59.833333333333336,59.842105263157904,60.05,60.142857142857125,59.3181818181818,59.56521739130436,59.416666666666664,59.160000000000004,58.42307692307692,57.777777777777786,57.42857142857143,56.827586206896555,56.63333333333334,56.25806451612904,55.75,55.54545454545455,55.11764705882352,54.885714285714286,54.777777777777786,54.45945945945947,54.184210526315795,54.07692307692308,53.7,53.51219512195122,53.28571428571428,53.09302325581395,53.06818181818181,52.84444444444445,52.76086956521739,52.91489361702128,52.64583333333333,52.51020408163265,52.540000000000006,52.21568627450982,52.32692307692308,52.67924528301887,53.03703703703705,53.32727272727273,53.625,53.98245614035089,54.20689655172414,54.457627118644055,54.60000000000001,54.77049180327869,55.08064516129032,55.269841269841265,55.437499999999986,55.61538461538463,55.787878787878796,56.04477611940298,56.294117647058826,56.52173913043477,56.72857142857141,56.95774647887323,57.125,57.31506849315069,57.45945945945947,57.666666666666664,57.881578947368425,57.92207792207792,58.11538461538463,58.189873417721515,58.3,58.333333333333336,58.19512195121952,58.28915662650603,58.25,58.2,58.19767441860465,58.21839080459769,58.13636363636364,58.14606741573034,58.05555555555556,58.01098901098901,58.03260869565217,57.95698924731183,57.95744680851065,57.90526315789474,57.833333333333336,57.80412371134021,57.79591836734694,57.727272727272734,57.739999999999995
#], marker="o", color='#0bf933', markerfacecolor="None",
#         markeredgecolor='#0bf933', markeredgewidth=0.8)
#plt.plot(x, [33.0,40.5,48.0,52.0,53.60000000000001,55.83333333333333,57.42857142857143,57.125,58.1111111111111,57.7,58.272727272727266,59.0,58.84615384615385,59.357142857142854,59.60000000000001,59.3125,59.82352941176471,59.8888888888889,59.842105263157904,60.0,60.09523809523809,59.272727272727266,59.43478260869564,59.166666666666664,58.67999999999999,57.96153846153847,57.333333333333336,57.07142857142857,56.48275862068965,56.3,55.93548387096773,55.437499999999986,55.242424242424235,54.82352941176471,54.60000000000001,54.500000000000014,54.18918918918918,53.921052631578945,53.94871794871794,53.64999999999999,53.390243902439025,53.19047619047619,52.88372093023257,52.79545454545455,52.777777777777786,52.56521739130436,52.44680851063829,52.20833333333333,52.183673469387756,52.18000000000001,51.76470588235294,51.76923076923076,52.05660377358491,52.42592592592594,52.727272727272734,53.03571428571429,53.40350877192982,53.63793103448275,53.89830508474576,54.05,54.22950819672131,54.54838709677419,54.74603174603173,54.921875,55.10769230769232,55.287878787878796,55.552238805970134,55.80882352941177,56.04347826086956,56.25714285714285,56.492957746478865,56.66666666666667,56.86301369863014,57.01351351351353,57.226666666666674,57.44736842105264,57.4935064935065,57.69230769230769,57.77215189873418,57.8875,57.92592592592591,57.792682926829265,57.891566265060234,57.857142857142875,57.81176470588234,57.81395348837209,57.83908045977013,57.76136363636364,57.7752808988764,57.68888888888888,57.64835164835165,57.673913043478265,57.602150537634415,57.6063829787234,57.5578947368421,57.489583333333336,57.4639175257732,57.45918367346938,57.39393939393939,57.230000000000004
#], marker="o", color='#7fa1ea', markerfacecolor="None",
#         markeredgecolor='#7fa1ea', markeredgewidth=0.8)
plt.plot(x, [33.0,41.5,50.0,53.5,55.8,57.999999999999986,59.28571428571429,58.875,59.8888888888889,59.3,59.63636363636364,60.333333333333336,60.0,60.42857142857143,60.60000000000001,60.25,60.705882352941174,60.66666666666667,60.631578947368425,60.8,59.71428571428574,59.04545454545455,59.30434782608695,59.166666666666664,58.919999999999995,58.96153846153847,58.96296296296295,58.642857142857125,58.689655172413794,58.36666666666666,58.25806451612904,58.3125,58.09090909090911,58.11764705882352,57.971428571428575,57.722222222222214,57.702702702702695,57.657894736842096,57.46153846153847,57.52499999999999,57.560975609756085,57.57142857142857,57.465116279069775,57.340909090909086,57.39999999999999,57.413043478260875,57.3404255319149,57.458333333333336,57.26530612244896,57.2,57.23529411764706,57.28846153846155,57.54716981132076,57.81481481481482,58.018181818181816,58.232142857142854,58.50877192982456,58.655172413793096,58.83050847457626,58.89999999999999,59.0,59.24193548387096,59.36507936507938,59.46875,59.58461538461539,59.6969696969697,59.89552238805969,60.088235294117645,60.26086956521739,60.41428571428571,60.59154929577464,60.70833333333333,60.84931506849315,60.94594594594595,61.10666666666667,61.27631578947368,61.272727272727266,61.42307692307692,61.45569620253165,61.52499999999999,61.27160493827161,61.170731707317074,60.8433734939759,60.65476190476191,60.48235294117647,60.26744186046513,60.03448275862068,59.909090909090914,59.69662921348314,59.58888888888889,59.439560439560424,59.22826086956523,59.118279569892465,58.93617021276596,58.81052631578947,58.70833333333333,58.56701030927836,58.40816326530613,58.31313131313131,58.14999999999999
], marker="o", color='#ff0000', markerfacecolor="None",
         markeredgecolor='#ff0000', markeredgewidth=0.8)
#plt.plot(x, [33.0,40.5,48.0,52.0,53.60000000000001,56.000000000000014,57.42857142857143,57.125,58.1111111111111,57.7,58.18181818181817,58.916666666666664,58.69230769230769,59.21428571428574,59.39999999999999,59.125000000000014,59.647058823529406,59.66666666666667,59.684210526315795,59.89999999999999,60.0,59.3181818181818,59.04347826086955,58.458333333333336,57.999999999999986,57.30769230769231,56.70370370370371,56.46428571428571,55.89655172413792,55.733333333333334,55.38709677419355,54.90625,54.727272727272734,54.32352941176471,54.114285714285714,54.02777777777777,53.729729729729726,53.473684210526315,53.38461538461537,53.05,52.829268292682926,52.54761904761905,52.55813953488372,52.38636363636364,52.2,52.021739130434796,51.95744680851065,51.5625,51.55102040816327,51.33999999999999,51.450980392156865,51.61538461538463,51.981132075471706,52.35185185185185,52.65454545454544,52.96428571428572,53.33333333333333,53.56896551724138,53.83050847457626,53.983333333333334,54.16393442622952,54.483870967741936,54.682539682539684,54.859375,55.04615384615384,55.227272727272734,55.492537313432834,55.75,55.98550724637681,56.2,56.43661971830987,56.6111111111111,56.80821917808218,56.95945945945947,57.17333333333333,57.394736842105274,57.44155844155843,57.64102564102565,57.72151898734178,57.83749999999999,57.876543209876544,57.74390243902438,57.8433734939759,57.80952380952381,57.76470588235294,57.76744186046513,57.79310344827586,57.71590909090911,57.73033707865169,57.64444444444443,57.604395604395606,57.6304347826087,57.559139784946225,57.56382978723404,57.51578947368421,57.447916666666664,57.42268041237113,57.41836734693878,57.35353535353535,57.36999999999999
#], marker="o", color='#000000', markerfacecolor="None",
#         markeredgecolor='#000000', markeredgewidth=0.8)
plt.plot(x, [33.0,39.5,48.33333333333333,52.25,54.8,57.166666666666664,58.57142857142857,58.25,59.333333333333336,58.8,59.18181818181817,59.916666666666664,59.61538461538463,60.07142857142857,60.266666666666666,59.9375,60.411764705882355,60.3888888888889,60.368421052631575,60.55,59.47619047619047,59.227272727272734,58.173913043478265,57.499999999999986,57.27999999999999,56.846153846153854,56.66666666666667,56.57142857142857,55.96551724137932,55.8,55.38709677419355,54.96875,54.78787878787877,54.23529411764706,54.0,53.91666666666667,53.75675675675676,53.552631578947384,53.46153846153847,53.125,52.829268292682926,52.76190476190477,52.76744186046511,52.75,52.62222222222222,52.56521739130436,52.574468085106375,52.25,52.22448979591837,52.22000000000001,52.27450980392156,52.42307692307692,52.75471698113209,53.12962962962963,53.41818181818182,53.75,54.052631578947356,54.27586206896551,54.50847457627118,54.64999999999999,54.819672131147556,55.11290322580645,55.317460317460316,55.500000000000014,55.676923076923075,55.86363636363636,56.11940298507464,56.367647058823536,56.59420289855073,56.8,57.014084507042256,57.18055555555556,57.36986301369863,57.51351351351353,57.72000000000001,57.934210526315795,57.97402597402596,58.166666666666664,58.24050632911393,58.35000000000001,58.296296296296305,58.13414634146342,58.18072289156625,58.119047619047606,57.98823529411764,58.0232558139535,57.942528735632195,57.8181818181818,57.764044943820224,57.60000000000001,57.46153846153847,57.44565217391304,57.322580645161295,57.36170212765957,57.33684210526316,57.36458333333333,57.27835051546391,57.24489795918366,57.18181818181817,57.14999999999999
], marker="o", color='#ffcc66', markerfacecolor="None",
         markeredgecolor='#ffcc66', markeredgewidth=0.8)


#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper le0t')
#plt.legend(['NB', 'Chi-Squared', 'FCBF', 'EFS', 'IG', 'OFS'], loc='‘lower right', fontsize='small', shadow=True, fancybox=True)
plt.legend(['NB', 'EFS', 'OFS'], loc='‘lower right', fontsize='small', shadow=True, fancybox=True)

plt.xlabel('Processed tuples', fontsize=12)
plt.ylabel('Accuracy (%)', fontsize=12)

#plt.grid(color='k', linestyle='-.', linewidth=0.4)
plt.xticks(np.arange(100, 11100, step=1000))
plt.yticks(np.arange(40, 110, step=10))

plt.tight_layout()

#plt.show()
plt.savefig('acc_recurrent_10.eps')