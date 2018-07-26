import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(500)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.gca().set_color_cycle(['blue'])

plt.plot([1000,2000,3000,4000,5000,6000,7000,8000,9000,9324], [26.10,54.25,82.57,110.95,139.51,168.28,196.76,225.09,253.51,263.354], marker="o", color='#ee0fc3', linewidth=1)
plt.plot([1000,2000,3000,4000,5000,6000,7000,8000,9000,9324], [83.93,169.55,255.42,342.07,429.09,516.04,603.35,689.13,775.12,803.65],  marker="o", color='#e5914b')
plt.plot([1000,2000,3000,4000,5000,6000,7000,8000,9000,9324], [84.98,171.07,257.46,344.62,431.41,518.09,605.33,693.18,780.74,809.551],  marker="o", color='#000000')
plt.plot([1000,2000,3000,4000,5000,6000,7000,8000,9000,9324], [81.86,165.73,249.32,333.43,417.64,502.03,586.37,670.63,754.95,782.85],  marker="o", color='#e7ade3')
plt.plot([1000,2000,3000,4000,5000,6000,7000,8000,9000,9324], [43.26,87.49,131.79,175.90,219.99,264.13,308.33,351.97,395.40,412.48],  marker="o", color='#ba2323')
plt.plot([1000,2000,3000,4000,5000,6000,7000,8000,9000,9324], [45.89,93.03,139.50,186.75,233.08,279.76,326.62,373.43,419.65,435.29],  marker="o", color='#3023ba')
plt.plot([1000,2000,3000,4000,5000,6000,7000,8000,9000,9324], [45.65,92.12,138.29,184.69,225.85,277.10,323.89,370.18,415.63,431.171],  marker="o", color='#d1db3f')


#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['NaiveBayes', 'MK-4', 'MK-10', 'MK-100',  'OFS-4','OFS-10', 'OFS-100'], loc='upper left')

plt.xlabel('Tuplas processadas', fontsize=12)
plt.ylabel('Tempo de de processamento (em segundos)', fontsize=12)

#plt.show()
plt.savefig('saved_charts/time_spam_data.png')
