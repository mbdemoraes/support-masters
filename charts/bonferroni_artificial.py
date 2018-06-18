import matplotlib.pyplot as plt
import numpy as np



x = [0,3,6]
x_labels = [0.2,3.2,6.2]
y = [1.437,2.0,2.56]
n = [1.437,2.0,2.56]
labels = ['NaiveBayes', 'OFS', 'MK']

plt.plot(x, y, 'ko')
# You can specify a rotation for the tick labels in degrees or with keywords.
plt.xticks(x, labels, rotation=30)

plt.axvline(x=0, linewidth='2', color='r', ymin=0.0, ymax=0.85)
plt.axhline(y=3.78, linestyle='--', xmin=0.0, xmax=1.0)


plt.legend(['Ranking Médio', 'Diferença Crítica'], loc='lower left', bbox_to_anchor= (0.0, 1.01), ncol=4, 
            borderaxespad=0, frameon=False)

plt.ylabel('Ranking médio', fontsize=12)

plt.axes().yaxis.grid(True) # Just y 

# Pad margins so that markers don't get clipped by the axes
plt.margins(0.2)
# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(bottom=0.15)

for i, txt in enumerate(n):
    plt.annotate(txt, (x_labels[i],y[i]))

plt.tight_layout()

#plt.show()
plt.savefig('saved_charts/bonferroni_artificial.png')
