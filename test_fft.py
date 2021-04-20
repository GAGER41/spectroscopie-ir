import scipy
import numpy as np
from matplotlib import pyplot as plt

## Jaune

position_j = r'C:\Users\gabri\Documents\Université\Session 4\Optique (lab)\spectroscopie ir\lumblanche-highres.txt'
#data = np.array(pd.read_csv(position, usecols=[3, 4])).transpose()
data_j = np.loadtxt(position_j, delimiter="	", skiprows=18, usecols=(1, 2)).transpose()

position_j = data_j[0]
_signal_j = data_j[1]-np.average(data_j[1])                               # ons osustrait la valeur moyenne pour enlever le pic à zéro de la fft
fourier_j = np.fft.fft(_signal_j)
freq_j = np.fft.fftfreq(len(data_j[0]), d=position_j[1]-position_j[0])      # pour trouver les fréquences du spectre
#freq = 2.9e8/freq
#plt.plot(position, _signal)
plt.plot(freq_j[:int(len(freq_j)/2)]*3e8*1e6, abs(fourier_j[:int(len(fourier_j)/2)]), 'y-')                                # On multiplie par c puis par 1e6 pour avoir des fréquences en Hz au lieu de 1/micron

plt.show()
## Bleu

position_b = r'C:\Users\gabri\Documents\Université\Session 4\Optique (lab)\spectroscopie ir\essai_6(bleu).txt'
#data = np.array(pd.read_csv(position, usecols=[3, 4])).transpose()
data_b = np.loadtxt(position_b, delimiter="	", skiprows=18, usecols=(1, 2)).transpose()

position_b = data_b[0]
_signal_b = data_b[1]-np.average(data_b[1])                               # ons osustrait la valeur moyenne pour enlever le pic à zéro de la fft
fourier_b = np.fft.fft(_signal_b)
freq_b = np.fft.fftfreq(len(data_b[0]), d=position_b[1]-position_b[0])      # pour trouver les fréquences du spectre
#plt.plot(position, _signal)
plt.plot(freq_b[:int(len(freq_b)/2)]*3e8*1e6, abs(fourier_b[:int(len(fourier_b)/2)]), 'b-')                                # On multiplie par c puis par 1e6 pour avoir des fréquences en Hz au lieu de 1/micron


## Rouge

position_r = r'C:\Users\gabri\Documents\Université\Session 4\Optique (lab)\spectroscopie ir\essai_6(rouge).txt'
#data = np.array(pd.read_csv(position, usecols=[3, 4])).transpose()
data_r = np.loadtxt(position_r, delimiter="	", skiprows=18, usecols=(1, 2)).transpose()

position_r = data_r[0]
_signal_r = data_r[1]-np.average(data_r[1])                               # ons osustrait la valeur moyenne pour enlever le pic à zéro de la fft
fourier_r = np.fft.fft(_signal_r)
freq_r = np.fft.fftfreq(len(data_r[0]), d=position_r[1]-position_r[0])      # pour trouver les fréquences du spectre
#freq = 2.9e8/freq
#plt.plot(position, _signal)
plt.plot(freq_r[:int(len(freq_r)/2)]*3e8*1e6, abs(fourier_r[:int(len(fourier_r)/2)]), 'r-')                                # On multiplie par c puis par 1e6 pour avoir des fréquences en Hz au lieu de 1/micron



# Donc, la fonction np.fft.fft permet de faire des transformées de fourier sur une matrice de data
# Scipy a peut-être aussi une fonction, mais elle n'a pas fonctionné ici
# freq en 1/d (d -> unités de position, microns ici)

# augmenter le pas diminue les chances d'avoir du bruit aux hautes fréquences
# augmenter le temps d'acquisition, même s'il se passe rien, augmente la résolution df (précision des fréquences dans l'espace de fourier)
# attention au facteur 2 introduit par le déplacement du miroir (c'est pas la position du miroir qui nous intéresse, mais le trajet optiqie)