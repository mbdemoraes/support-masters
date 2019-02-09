
# libraries
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-darkgrid')
 
# set width of bar
barWidth = 0.25
 
# set height of bar
bars1 = [311.5037372338, 457.48213390560005,429.3094015973999,301.68275571350006,517.3760303541001,405.94501224009997]
bars2 = [311.5037372338, 394.72494998929994,313.08324853930003,301.3268716694,401.5464570163,320.4454066849]
bars3 = [311.5037372338, 314.7190784743,355.4085493796,294.92905812499987,459.8241428018,283.21399330279996]

# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
 
# Make the plot
plt.bar(r1, bars1, color='#cb5b5a', width=barWidth, edgecolor='white', label='Window 100')
plt.bar(r2, bars2, color='#2d72ed', width=barWidth, edgecolor='white', label='Window 500')
plt.bar(r3, bars3, color='#3cb371', width=barWidth, edgecolor='white', label='Window 1000')
 
# Add xticks on the middle of the group bars
plt.xlabel('Algorithms', fontsize=12)
plt.ylabel('Time (s)', fontsize=12)
plt.xticks([r + barWidth for r in range(len(bars1))], ['NB', 'Chi', 'FCBF', 'EFS', 'IG', 'OFS'])
 
# Create legend & Show graphic
plt.legend()

plt.tight_layout()

plt.savefig('time_spam_assassin_10.eps')
