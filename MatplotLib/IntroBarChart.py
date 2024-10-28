import matplotlib.pyplot as plt
import numpy as np

labels = ["A","B"] #labels means the name you want to give.
values = [1,2] #values means the height of the bar.

bars = plt.bar(labels,values)

bars[0].set_hatch('/') #set the design inside the bars.
bars[1].set_hatch('-')

plt.show()