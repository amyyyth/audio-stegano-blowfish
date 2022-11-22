import matplotlib.pyplot as plt
from scipy.io.wavfile import read


input_data1 = read("cover_trim.wav")
audio1 = input_data1[1]
input_data2 = read("encoded.wav")
audio2 = input_data2[1]

plt.subplot(2,1,1)
plt.title("OG audio")
plt.plot(audio1)
plt.subplot(2,1,2)
plt.title("encoded audio")
plt.plot(audio2)

plt.show()