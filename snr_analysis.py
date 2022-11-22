import librosa
import numpy as np
import math
from encoder import *
from blowfish import *
import matplotlib.pyplot as plt

SNR = 10

signal, sr = librosa.load(r"C:\Users\amith\Code\crypto\audio-stegano-blowfish\cover.wav")
print(sr)
enc_signal, sr = librosa.load(r"C:\Users\amith\Code\crypto\audio-stegano-blowfish\encoded.wav")

a = plt.psd(signal,sr)
print(len(a))
plt.plot(a)
plt.show()

print(len(a[0]))

# print(sr)

# RMS_sig = math.sqrt(np.mean(signal**2))

# RMS_noise = math.sqrt((RMS_sig**2)/(10**(SNR/10)))

# STD_noise = RMS_noise

# noise = np.random.normal(0, STD_noise, signal.shape[0])





# key = b"this is a secret key or is it"

# noisy_signal = noise + signal

# print(type(noisy_signal))

# with open('encoded_noisy.wav', mode='bw+') as f:
#         f.write(noisy_signal.tobytes())

# signal, sr = librosa.load(r"C:\Users\amith\Code\crypto\audio-stegano-blowfish\encoded.wav")
# print(sr)
# signal, sr = audioread(r"C:\Users\amith\Code\crypto\audio-stegano-blowfish\encoded_noisy.wav")
# print(sr)

# s_key_rec = end_decoder(r"C:\Users\amith\Code\crypto\audio-stegano-blowfish\encoded_noisy.wav")

# s_key_dec = bf_dec(s_key_rec,key)

# cp = decode(r"C:\Users\amith\Code\crypto\audio-stegano-blowfish\encoded_noisy.wav",(s_key_dec))

# msg_rec = (bf_dec(cp,key))

# print(msg_rec)
