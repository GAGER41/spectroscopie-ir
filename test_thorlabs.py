import scipy
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

position = r'C:\Users\gabri\Documents\Université\Session 4\Optique (lab)\spectroscopie ir\lumiere_blanche_thorlabs2.csv'
#data_j = np.loadtxt(position_j, delimiter="	", skiprows=18, usecols=(1, 2)).transpose()
data = pd.read_csv(position)
#data = np.loadtxt(position, delimiter="    ")
data = np.array(data).transpose()
print(data.size)
temps = data[0]
_signal = data[1]

#print(data)

plt.plot(temps/1000, _signal)
plt.show()