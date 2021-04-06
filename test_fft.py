import scipy
import numpy as np
from matplotlib import pyplot as plt

position = r'C:\Users\gabri\Documents\Université\Session 4\Optique (lab)\spectroscopie ir\lumblanche-highres.txt'
#data = np.array(pd.read_csv(position, usecols=[3, 4])).transpose()
data = np.loadtxt(position, delimiter="	", skiprows=18, usecols=(1, 2)).transpose()

position = data[0]
_signal = data[1]-np.average(data[1])                               # ons osustrait la valeur moyenne pour enlever le pic à zéro de la fft
fourier = np.fft.fft(_signal)
freq = np.fft.fftfreq(len(data[0]), d=position[1]-position[0])      # pour trouver les fréquences du spectre
#plt.plot(position, _signal)
plt.plot(freq[:int(len(freq)/2)]*3e8*1e6, abs(fourier[:int(len(fourier)/2)]))                                # On multiplie par c puis par 1e6 pour avoir des fréquences en Hz au lieu de 1/micron
plt.show()

# Donc, la fonction np.fft.fft permet de faire des transformées de fourier sur une matrice de data
# Scipy a peut-être aussi une fonction, mais elle n'a pas fonctionné ici
# freq en 1/d (d -> unités de position, microns ici)

# augmenter le pas diminue les chances d'avoir du bruit aux hautes fréquences
# augmenter le temps d'acquisition, même s'il se passe rien, augmente la résolution df (précision des fréquences dans l'espace de fourier)
# attention au facteur 2 introduit par le déplacement du miroir (c'est pas la position du miroir qui nous intéresse, mais le trajet optiqie)