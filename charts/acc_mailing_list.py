import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(1000)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.gca().set_color_cycle(['blue'])

plt.plot([1000,2000,3000,4000,5000,5995], [75.10,80.15,82.66,83.3,83.98,84.60], marker="o", color='#ee0fc3', linewidth=1)
plt.plot([1000,2000,3000,4000,5000,5995], [54.23,57.65,59.54,59.75,60.15,60.23],  marker="o", color='#e5914b')
plt.plot([1000,2000,3000,4000,5000,5995], [67.42,68.92,69.93,69.07,67.73,66.31],  marker="o", color='#000000')
plt.plot([1000,2000,3000,4000,5000,5995], [82.11,84.98,86.28,84.76,82.82,80.79],  marker="o", color='#e7ade3')
plt.plot([1000,2000,3000,4000,5000,5995], [53.68,51.6,51.52,52.22,52.91,53.30],  marker="o", color='#ba2323')
plt.plot([1000,2000,3000,4000,5000,5995], [53.70,51.85,51.76,52.5,53.22,53.76],  marker="o", color='#3023ba')
plt.plot([1000,2000,3000,4000,5000,5995], [55.75,54.43,55.39,55.84,56.49,56.92],  marker="o", color='#d1db3f')


#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['NaiveBayes', 'MK-4', 'MK-10', 'MK-100',  'OFS-4','OFS-10', 'OFS-100'], loc='lower left', bbox_to_anchor= (0.0, 1.01), ncol=4, 
            borderaxespad=0, frameon=False)

plt.xlabel('Tuplas processadas', fontsize=12)
plt.ylabel('Acurácia (em %)', fontsize=12)

#plt.show()
plt.savefig('saved_charts/acc_mailing_list.png')
