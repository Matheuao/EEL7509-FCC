"""
O arquivo “vibracaoviga.npz” (disponível no Moodle) contém o
sinal de aceleração (amostrado em 250 Hz) em uma viga submetida a uma
vibração sinusoidal causada por um motor girando em velocidade constante. Em
um certo momento, um sistema de controle de vibração é ativado, reduzindo
significativamente a intensidade da vibração na viga. Plote o referido sinal no
tempo e também o seu espectrograma e identifique:
• A frequência da vibração sinusoidal que afetava a viga;
• O instante de tempo no qual o sistema de controle é ativado.
Se necessário, ajuste os parâmetros do método scipy.signal.spectrogram() de
forma a melhorar a visibilidade do espectrograma obtido. Além disso, para abrir
o arquivo utilize dados = np.load('vibracaoviga.npz') e, com isso, os dados
estarão disponíveis em dados['vibviga'] .
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

data = np.load("vibracaoviga.npz")

frequencies, times, Sxx = spectrogram(data["vibviga"])

fig, axes = plt.subplots(2,1)

axes[0].plot(data["vibviga"])
axes[0].annotate( 'sistema de controle ativado',
    xy=(30100, 0.2),
    xytext=(32000, 1),
    arrowprops=dict(
    arrowstyle='->',
    connectionstyle='arc3,rad=0.2',
    color='red'
    ),
    fontsize=10,
    color='red'
)
axes[0].set_xlabel("Time (s)")
axes[0].set_ylabel("Amplitude")

cax =  axes[1].pcolormesh( times, frequencies, 10 * np.log10(Sxx),shading = "gouraud")
fig.colorbar(cax,ax =axes[1], label ="Intensity (dB)")

axes[1].annotate( 'frequência de vibração que afeta a viga',
    xy=(30100, 0.09),
    xytext=(30500, 0.15),
    arrowprops=dict(
    arrowstyle='->',
    connectionstyle='arc3,rad=0.2',
    color='red'
    ),
    fontsize=10,
    color='red'
)
axes[1].set_xlabel("Time (s)")
axes[1].set_ylabel("Frequency (Hz)")


fig.set_size_inches(10, 5)
fig.tight_layout()
fig.show()


