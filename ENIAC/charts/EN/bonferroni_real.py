import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Patch


x = [1, 2, 3, 4, 5, 6, 7]
x_labels = [1.2, 2.2, 3.2, 4.2, 5.2, 6.2, 7.2]
y = [1.875, 2.5, 3.625, 3.875, 4.875,5.0,6.25]
n = [1.875, 2.5, 3.625, 3.875, 4.875,5.0,6.25]
labels = ['IG-100', 'IG-10', 'IG-4', 'NaiveBayes', 'OFS-10', 'OFS-100', 'OFS-4']


# You can specify a rotation for the tick labels in degrees or with keywords.
plt.xticks(x, labels, rotation=30)

plt.axvline(x=1, linewidth='2', color='r', ymin=0.0, ymax=0.45)
plt.axvline(x=2, linewidth='2', color='r', ymin=0.0, ymax=0.51)
plt.axvline(x=3, linewidth='2', color='r', ymin=0.09, ymax=0.62)
plt.axvline(x=4, linewidth='2', color='r', ymin=0.12, ymax=0.65)
plt.axvline(x=5, linewidth='2', color='r', ymin=0.22, ymax=0.75)
plt.axvline(x=6, linewidth='2', color='r', ymin=0.23, ymax=0.76)
plt.axvline(x=7, linewidth='2', color='r', ymin=0.36, ymax=0.88)
plt.plot(x, y, 'ko')

legend_elements = [Line2D([0], [0], marker='o', color='k', label='Average rank',
                          markersize=8, linestyle=''),
                   Line2D([0], [0], color='r', linewidth='3', label='Critical value'
                          )
                  ]


plt.yticks(np.arange(0, 11, step=1))
plt.ylim(0,10)


plt.legend(handles=legend_elements, loc='lower left', bbox_to_anchor= (0.0, 1.01), ncol=4, 
            borderaxespad=0, frameon=False)

plt.ylabel('Average rank', fontsize=12)

plt.axes().yaxis.grid(True) # Just y 

# Pad margins so that markers don't get clipped by the axes
plt.margins(0.2)
# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(bottom=0.15)

for i, txt in enumerate(n):
    plt.annotate(txt, (x_labels[i],y[i]))

plt.tight_layout()

#plt.show()
plt.savefig('bonferroni_real.png')
