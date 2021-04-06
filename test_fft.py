import scipy
import numpy as np
from matplotlib import pyplot as plt

position = r'C:\Users\gabri\Documents\Université\Session 4\Optique (lab)\spectroscopie ir\test_lum_blanche.txt'
#data = np.array(pd.read_csv(position, usecols=[3, 4])).transpose()
data = np.loadtxt(position, delimiter="	", skiprows=18, usecols=(1, 2)).transpose()

position = data[0]
_signal = data[1]
fourier = np.fft.fft(_signal)
#plt.plot(position, _signal)
plt.plot(position, fourier)
plt.show()

# Donc, la fonction np.fft.fft permet de faire des transformées de fourier sur une matrice de data