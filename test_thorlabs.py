import scipy
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


    ## Lumière blanche
position = r'C:\Users\gabri\Documents\Université\Session 4\Optique (lab)\spectroscopie ir\Tests_20-04-2021\lumiere_2.csv'
#position = r'C:\Users\Sandrine Poulin\OneDrive\Documents\Hiver_2021\Labs TPOP\spectroscopie-ir\Tests_20-04-2021\lumiere_blanche_240s.csv'
data = pd.read_csv(position)                # lecture du csv
data = np.array(data).transpose()           # conversion du data en array

## On ne connait pas le déplacement, mais les acquisitions sont faites sur 2 minutes (120 secondes)
## Par contre, on connait le temps entre les acquisitions et le pas, donc 1 micros-pas = 0.1 micron, à chaque 80 ms
## Vitesse de déplacement = 0.1micron/80ms, donc on peut connaître le déplacement total lors de l'acquisition

vitesse = 0.1e-6/80e-3 #m/s
distance = (data[0][-1] - data[0][0]) / 1000 * 2 * vitesse #m                         # temps en ms, /1000, puis * 2 * vitesse

temps = data[0] #s                                                     # temps
position = np.linspace(0, distance, len(temps))                        # matrice position généré avec le temps et la vitesse
_signal = data[1] - np.average(data[1]) #watt                          # signal, puissance

fourier = np.fft.fft(_signal)                                          # fft du signal
freq = np.fft.fftfreq(len(position), d=position[1]-position[0])        # on génère une matrice des fréquences dans l'espace de Fourier, en 1/dx (unités),  donc m^-1

# on garde seulement la 2e moitié qui est positive
lo_pos =  freq[:int(len(freq)/2)]                                      # si on inverse (^-1), on obtient des longueurs d'onde
fourier_pos = abs(fourier[:int(len(fourier)/2)])


    ## Échantillon
for i in ['J', 'M', 'V']: #range(1, 11):

    # coeff 20 avril, prendre lumiere_2.csv
    """if i == 1:
        j = 0.9
    elif i == 2:
        j = 0.9
    elif i == 3:
        j = 0.93
    elif i == 4:
        j = 0.9
    elif i == 5:
        j = 0.93
    elif i == 6:
        j = 0.94
    elif i == 7:
        j = 0.98
    elif i == 8:
        j = 0.99
    elif i == 9:
        j = 0.99
    elif i == 10:
        j = 1.01"""
    # coeff pour 20 avril, mais tests _2, lumiere_2.csv
    """if i == 2:
        j = 1.02
    elif i == 6:
        j = 1.06
    elif i == 9:
        j = 1.03"""
    # bouésson 13 avril, prendre lumiere_blanche_thorlabs2_120s.csv
    """if i == "Gin":
        j = 1.1
    elif i == "Jack":
        j = 1.12
    elif i == "Vodka":
        j = 1.12"""
    # 13 avril, A1-2-3-6, lumiere_blanche_thorlabs2_120s.csv
    """if i == 1:
        j = 1.04
    elif i == 2:
        j = 1.04
    elif i == 3:
        j = 1.08
    elif i == 6:
        j = 1.05"""
    # 13 avril, A4-5-7-8, lumiere_2.csv   -> trop dégueu, pas plottés
    """if i == 4:
        j = 1.1
    elif i == 5:
        j = 1.1
    elif i == 7:
        j = 1.1
    elif i == 8:
        j = 1.1"""
    # bouésson, 20 avril, lumiere_2.csv
    if i == "J":
        j = 1 #1.08
        k = "Jack"
    elif i == "M":
        j = 1 #1.02
        k = "Midori"
    elif i == "V":
        j = 1 #0.99
        k = 'Vodka'

    position_e = r'C:\Users\gabri\Documents\Université\Session 4\Optique (lab)\spectroscopie ir\Tests_20-04-2021\{}_240s.csv'.format(i)
    #position_e = r'C:\Users\Sandrine Poulin\OneDrive\Documents\Hiver_2021\Labs TPOP\spectroscopie-ir\Tests_20-04-2021\A9_240s.csv'
    data_e = pd.read_csv(position_e)                # lecture du csv
    data_e = np.array(data_e).transpose()           # conversion du data en array

    ## On ne connait pas le déplacement, mais les acquisitions sont faites sur 2 minutes (120 secondes)
    ## Par contre, on connait le temps entre les acquisitions et le pas, donc 1 micros-pas = 0.1 micron, à chaque 80 ms
    ## Vitesse de déplacement = 0.1micron/80ms, donc on peut connaître le déplacement total lors de l'acquisition

    vitesse_e = 0.1e-6/80e-3
    distance_e = (data_e[0][-1] - data_e[0][0]) / 1000 * 2 * vitesse_e                         # temps en ms, /1000, puis * 2 * vitesse

    temps_e = data_e[0]                                                       # temps
    position_e = np.linspace(0, distance_e, len(temps_e))                     # matrice position généré avec le temps et la vitesse
    _signal_e = data_e[1] - np.average(data_e[1])                             # signal, puissance

    fourier_e = np.fft.fft(_signal_e)                                         # fft du signal
    freq_e = np.fft.fftfreq(len(position_e), d=(position_e[1]-position_e[0])*j)     # on génère une matrice des fréquences dans l'espace de Fourier, en 1/dx (unités),  donc m^-1

    # on garde seulement la 2e moitié qui est positive
    lo_pos_e =  freq_e[:int(len(freq_e)/2)]                                   # si on inverse (^-1), on obtient des longueurs d'onde
    fourier_pos_e = abs(fourier_e[:int(len(fourier_e)/2)])

    # Spectre d'absorption normalisé
    fourier_pos_t = fourier_pos_e[:1000] / fourier_pos[:1000]
    #fourier_pos_t = (fourier_pos[:200]-fourier_pos_e[:200])/fourier_pos[:200]

    #plt.plot(freq[:int(len(freq)/2)]*3e8*1e6, abs(fourier[:int(len(fourier)/2)]))
    plt.plot(lo_pos_e[:1000] / 100, fourier_pos_t*100, label ="Échantillon {}".format(k))
    #plt.plot(lo_pos / 100, fourier_pos, "k-", label="Lumière blanche")
    #plt.plot(lo_pos_e/100, fourier_pos_e, "k--", label="Échantillon {}".format(i))
    plt.legend()
    plt.xlim(0,5000)
    plt.ylim(0,1000)
    plt.xlabel("nombre d'onde (1/cm)")
    plt.ylabel("transmission (%)")
    #plt.savefig(r'C:\Users\Sandrine Poulin\OneDrive\Documents\Hiver_2021\Labs TPOP\spectroscopie-ir\Analyse (png)\S2_spectre.png', dpi = 600)
#plt.savefig("spectres_boissons_13avril.png", bbox_inches='tight',dpi=600)
plt.show()