import scipy
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

# Lumière blanche
position = r'C:\Users\gabri\Documents\Université\Session 4\Optique (lab)\spectroscopie ir\Tests_20-04-2021\lumiere_blanche_240s.csv'
#position = r'C:\Users\Sandrine Poulin\OneDrive\Documents\Hiver_2021\Labs TPOP\spectroscopie-ir\Tests_20-04-2021\lumiere_blanche_240s.csv'
data = pd.read_csv(position)                # lecture du csv
data = np.array(data).transpose()           # conversion du data en array

## On ne connait pas le déplacement, mais les acquisitions sont faites sur 2 minutes (120 secondes)
## Par contre, on connait le temps entre les acquisitions et le pas, donc 1 micros-pas = 0.1 micron, à chaque 80 ms
## Vitesse de déplacement = 0.1micron/80ms, donc on peut connaître le déplacement total lors de l'acquisition

vitesse = 0.1e-6/80e-3 #m/s
distance = 240 * vitesse #m

temps = data[0] #s                                                     # temps
position = np.linspace(0, distance, len(temps))                        # matrice position généré avec le temps et la vitesse
_signal = data[1] - np.average(data[1]) #watt                          # signal, puissance

fourier = np.fft.fft(_signal)                                       # fft du signal
freq = np.fft.fftfreq(len(position), d=position[1]-position[0])     # on génère une matrice des fréquences dans l'espace de Fourier, en 1/dx (unités),  donc m^-1

# on garde seulement la 2e moitié qui est positive
lo_pos =  freq[:int(len(freq)/2)]                              # si on inverse (^-1), on obtient des longueurs d'onde
fourier_pos = abs(fourier[:int(len(fourier)/2)])

#échantillon
position_e = r'C:\Users\gabri\Documents\Université\Session 4\Optique (lab)\spectroscopie ir\Tests_20-04-2021\A10_240s.csv'
#position_e = r'C:\Users\Sandrine Poulin\OneDrive\Documents\Hiver_2021\Labs TPOP\spectroscopie-ir\Tests_20-04-2021\A9_240s.csv'
data_e = pd.read_csv(position_e)                # lecture du csv
data_e = np.array(data_e).transpose()           # conversion du data en array

## On ne connait pas le déplacement, mais les acquisitions sont faites sur 2 minutes (120 secondes)
## Par contre, on connait le temps entre les acquisitions et le pas, donc 1 micros-pas = 0.1 micron, à chaque 80 ms
## Vitesse de déplacement = 0.1micron/80ms, donc on peut connaître le déplacement total lors de l'acquisition

vitesse_e = 0.1e-6/80e-3
distance_e = 240 * vitesse_e

temps_e = data_e[0]                                                     # temps
position_e = np.linspace(0, distance_e, len(temps_e))                     # matrice position généré avec le temps et la vitesse
_signal_e = data_e[1] - np.average(data_e[1])                             # signal, puissance

fourier_e = np.fft.fft(_signal_e)                                       # fft du signal
freq_e = np.fft.fftfreq(len(position_e), d=position_e[1]-position_e[0])     # on génère une matrice des fréquences dans l'espace de Fourier, en 1/dx (unités),  donc m^-1

# on garde seulement la 2e moitié qui est positive
lo_pos_e =  freq_e[:int(len(freq_e)/2)]                              # si on inverse (^-1), on obtient des longueurs d'onde
fourier_pos_e = abs(fourier_e[:int(len(fourier_e)/2)])

#Spectr d'absorption
fourier_pos_t = fourier_pos[:200] / fourier_pos_e[:200]

#plt.plot(freq[:int(len(freq)/2)]*3e8*1e6, abs(fourier[:int(len(fourier)/2)]))
plt.plot(lo_pos[:200] / 100, fourier_pos_t[:200], label = 'A1', color= 'black')
plt.xlim(1500,4000)
plt.xlabel("nombre d'onde (1/cm)")
#plt.savefig(r'C:\Users\Sandrine Poulin\OneDrive\Documents\Hiver_2021\Labs TPOP\spectroscopie-ir\Analyse (png)\S2_spectre.png', dpi = 600)
plt.show()