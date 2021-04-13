import scipy
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

position = r'C:\Users\gabri\Documents\Université\Session 4\Optique (lab)\spectroscopie ir\lumiere_blanche_thorlabs2.csv'
data = pd.read_csv(position)                # lecture du csv
data = np.array(data).transpose()           # conversion du data en array


## On ne connait pas le déplacement, mais les acquisitions sont faites sur 2 minutes (120 secondes)
## Par contre, on connait le temps entre les acquisitions et le pas, donc 1 micros-pas = 0.1 micron, à chaque 80 ms
## Vitesse de déplacement = 0.1micron/80ms, donc on peut connaître le déplacement total lors de l'acquisition

vitesse = 0.1e-6/80e-3
distance = 120 * vitesse

temps = data[0]                                                     # temps
position = np.linspace(0, distance, len(temps))                     # matrice position généré avec le temps et la vitesse
_signal = data[1] - np.average(data[1])                             # signal, puissance

fourier = np.fft.fft(_signal)                                       # fft du signal
freq = np.fft.fftfreq(len(position), d=position[1]-position[0])     # on génère une matrice des fréquences dans l'espace de Fourier

# on garde seulement la 2e moitié qui est positive

lo_pos = 3e8 / freq[:int(len(freq)/2)]                              # *3e8*1e6
fourier_pos = abs(fourier[:int(len(fourier)/2)])

#plt.plot(freq[:int(len(freq)/2)]*3e8*1e6, abs(fourier[:int(len(fourier)/2)]))           #on plot seulement la deuxième moitié, pas les fréquences négatives.
plt.plot(lo_pos[:400], fourier_pos[:400])
plt.show()

