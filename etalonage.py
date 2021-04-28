import numpy as np
from matplotlib import pyplot as plt

conc = np.array([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])
transm = np.array([7.77, 25.18, 30.3, 19.4, 32.21, 45.94, 401.47, 75.24, 113.14, 234.55])

plt.plot(conc, transm, 'k.')
plt.xlabel("concentration en éthanol (%v/v)")
plt.ylabel("transmission (%)")
#plt.savefig("etalonage_20avril.png", bbox_inches='tight',dpi=600)
plt.show()