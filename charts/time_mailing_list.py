import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(500)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.gca().set_color_cycle(['blue'])

plt.plot([1000,2000,3000,4000,5000,5995], [19.10,39.52,60.02,80.71,101.40,122.15], marker="o", color='#ee0fc3', linewidth=1)
plt.plot([1000,2000,3000,4000,5000,5995], [58.98,113.16,173.37,233.72,294.15,354.26],  marker="o", color='#e5914b')
plt.plot([1000,2000,3000,4000,5000,5995], [63.86,128.75,194.32,260.08,326.34,392.68],  marker="o", color='#000000')
plt.plot([1000,2000,3000,4000,5000,5995], [58.89,119.08,179.56,240.50,301.67,362.56],  marker="o", color='#e7ade3')
plt.plot([1000,2000,3000,4000,5000,5995], [32.13,65.06,98.00,130.49,167.77,195.18],  marker="o", color='#ba2323')
plt.plot([1000,2000,3000,4000,5000,5995], [31.71,64.09,96.53,128.95,161.18,193.04],  marker="o", color='#3023ba')
plt.plot([1000,2000,3000,4000,5000,5995], [32.14,65.38,98.31,131.68,164.73,197.67],  marker="o", color='#d1db3f')


#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['NaiveBayes', 'MK-4', 'MK-10', 'MK-100',  'OFS-4','OFS-10', 'OFS-100'], loc='upper left')

plt.xlabel('Tuplas processadas', fontsize=12)
plt.ylabel('Tempo de de processamento (em segundos)', fontsize=12)

#plt.show()
plt.savefig('saved_charts/time_mailing_list.png')
