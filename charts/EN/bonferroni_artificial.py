import matplotlib.pyplot as plt
import numpy as np

from matplotlib.lines import Line2D
from matplotlib.patches import Patch

x = [0,3,6]
x_labels = [0.2,3.2,6.2]
y = [1.437,2.0,2.56]
n = [1.437,2.0,2.56]
labels = ['NaiveBayes', 'OFS', 'IG']

# You can specify a rotation for the tick labels in degrees or with keywords.
plt.xticks(x, labels, rotation=30)

plt.axvline(x=0, linewidth='2', color='r', ymin=0.0, ymax=0.37)
plt.axvline(x=3, linewidth='2', color='r', ymin=0.0, ymax=0.43)
plt.axvline(x=6, linewidth='2', color='r', ymin=0.0, ymax=0.49)
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
plt.savefig('bonferroni_artificial.png')
