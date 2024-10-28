import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [1,2,3]
y = [2,4,6]

x2 = np.arange(0,4.5,0.5)
plt.plot(x2[:5],x2[:5]**2,label='x^2 simple half',color='blue',marker='.',markersize=10)
plt.plot(x2[4:],x2[4:]**2,label='x^2 dotted half',color='blue',marker='.',markersize=10,linestyle='--')
plt.plot()
plt.plot(x,y,label='2x',color='red',marker='.',markersize=10,markeredgecolor='black')
plt.title("Graph",fontdict={'fontname':'poppins','fontsize':20})
plt.xlabel("x-axis.")
plt.ylabel("y-axis.")
# plt.xticks([0,1,2,3])
# plt.yticks([0,2,4,6])
plt.savefig('myFirstGraph.png',dpi=300)#save the graph to current directory
plt.legend()#to show the label.
plt.show()