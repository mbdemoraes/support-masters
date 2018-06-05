import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(500)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.gca().set_color_cycle(['blue'])

plt.plot([1000,2000,3000,4000,5000,6000,7000,8000,9000,9324], [74.6,59.8,54.06,58.17,62.52,66.41,68.97,72.06,74.21,74.57], marker="o", color='#ee0fc3')
plt.plot([1000,2000,3000,4000,5000,6000,7000,8000,9000,9324], [83.71,71.89,77.35,78.68,80.25,81.98,82.10,83.86,85.57,85.81],  marker="o", color='#e5914b')
plt.plot([1000,2000,3000,4000,5000,6000,7000,8000,9000,9324], [90.6,78.43,82.49,83.28,84.43,85.62,85.82,87.24,88.59,88.73],  marker="o", color='#000000')
plt.plot([1000,2000,3000,4000,5000,6000,7000,8000,9000,9324], [87.49,76.62,81.23,82.83,84.33,85.58,85.84,87.09,88.48,88.56],  marker="o", color='#e7ade3')
plt.plot([1000,2000,3000,4000,5000,6000,7000,8000,9000,9324], [83.04,66.67,59.01,63.03,66.82,69.37,70.16,72.99,75.71,76.16],  marker="o", color='#ba2323')
plt.plot([1000,2000,3000,4000,5000,6000,7000,8000,9000,9324], [90.91,71.11,64.27,66.33,69.02,71.14,72.49,74.92,77.34,77.37],  marker="o", color='#3023ba')
plt.plot([1000,2000,3000,4000,5000,6000,7000,8000,9000,9324], [94.26,74.77,68.41,68.27,69.00,71.24,72.48,74.67,76.33,76.56],  marker="o", color='#d1db3f')


#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['NaiveBayes', 'MK-4', 'MK-10', 'MK-100',  'OFS-4','OFS-10', 'OFS-100'], loc='‘lower right', fontsize='small')

plt.xlabel('Tuplas processadas', fontsize=12)
plt.ylabel('Acurácia (%)', fontsize=12)

#plt.show()
plt.savefig('saved_charts/acc_spam_data.png')
