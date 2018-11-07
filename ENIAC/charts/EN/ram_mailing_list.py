import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(500)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.gca().set_color_cycle(['blue'])

plt.plot([1000,2000,3000,4000,5000,5995],[0.0000980607203361895,0.0002031287,0.0003087446,0.0004155703,0.0005225273,0.0006299437], marker="o", color='#ee0fc3')
plt.plot([1000,2000,3000,4000,5000,5995], [0.0003034524,0.0005829221,0.0008938019,0.0012060289,0.0015190419,0.0018307783],  marker="o", color='#e5914b')
plt.plot([1000,2000,3000,4000,5000,5995], [0.0003258851,0.000657652,0.0009933594,0.0013305829,0.0016708014,0.0020118088],  marker="o", color='#000000')
plt.plot([1000,2000,3000,4000,5000,5995], [0.0003030382,0.000613413,0.0009256492,0.0012408511,0.0015576526,0.0018733304],  marker="o", color='#e7ade3')
plt.plot([1000,2000,3000,4000,5000,5995], [0.0001651457,0.000334794,0.0005046977,0.0006726361,0.0008397524,0.0010077332],  marker="o", color='#ba2323')
plt.plot([1000,2000,3000,4000,5000,5995], [0.0001629341,0.0003296034,0.0004968681,0.0006643748,0.0008310614,0.0009960687],  marker="o", color='#3023ba')
plt.plot([1000,2000,3000,4000,5000,5995], [0.0001651001,0.0003362474,0.0005060502,0.0006785065,0.0008495806,0.0010208291],  marker="o", color='#d1db3f')


#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['NaiveBayes', 'MK-4', 'MK-10', 'MK-100',  'OFS-4','OFS-10', 'OFS-100'], loc='upper left')

plt.xlabel('Tuplas processadas', fontsize=12)
plt.ylabel('Custo do modelo (RAM-Horas)', fontsize=12)

#plt.show()
plt.tight_layout()
plt.savefig('saved_charts/ram_mailing_list.png')
