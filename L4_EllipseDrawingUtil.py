import numpy as np
%matplotlib inline
from matplotlib import pyplot as plt 
data = np.array([
[0, 4], [1, 4], [2, 4], [3, 4], [4, 3], [5, 3], [6, 3], [7, 2], [8, 1], [0, 4], [-1, 4], [-2, 4], [-3, 4], [-4,
3], [-5, 3], [-6, 3], [-7, 2], [-8, 1], [0, -4], [-1, -4], [-2, -4], [-3, -4], [-4, -3], [-5, -3], [-6, -3], [-7, -2],
[-8, -1], [0, -4], [1, -4], [2, -4], [3, -4], [4, -3], [5, -3], [6, -3], [7, -2], [8, -1],
])
x, y = data.T 
plt.xlim(0, 15)
plt.ylim(0, 15) 
plt.axis('equal') 
plt.scatter(x,y) 
plt.show()
