from utils import *
from encoder import *
from snr_analysis import *
import matplotlib.pyplot as plt
import string
import random
from tqdm import tqdm

str_size = 1000

msg =  ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=str_size))
msg = msg.encode()
cover = "cover_trim.wav"

# SNR vs bit depth

bit_depths = list(range(1,9))
snrs_old = []
snrs_new = []

print("calculating for different bit depths: ")
for i in tqdm(range(len(bit_depths))):
    encoded_old = encode(msg, cover, bit_depths[i])
    snr_old = snr_analysis("cover_trim.wav","encoded.wav")
    snrs_old.append(snr_old)
    encoded_new = encode_new(msg, cover, bit_depths[i])
    snr_new = snr_analysis("cover_trim.wav","encoded.wav")
    snrs_new.append(snr_new)


plt.figure(1)
plt.title("Comparison of schemes for bit depth")
plt.xlabel("bit depths")
plt.ylabel("SNR in dB")
new, = plt.plot(bit_depths,snrs_new, label = "New scheme")
old, = plt.plot(bit_depths,snrs_old, label = "Old scheme")
plt.legend(handles = [new, old])
# plt.show()


# SNR vs message length

msglens = list(range(100,800))
snrs_old = []
snrs_new = []
print("\n Calculating for different message lengths: ")
for i in tqdm(range(len(msglens))):
    msg =  ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=msglens[i]))
    msg = msg.encode()
    encoded_old = encode(msg, cover, 5)
    snr_old = snr_analysis("cover_trim.wav","encoded.wav")
    snrs_old.append(snr_old)
    encoded_new = encode_new(msg, cover,5)
    snr_new = snr_analysis("cover_trim.wav","encoded.wav")
    snrs_new.append(snr_new)


plt.figure(2)
plt.title("Comparison of schemes for msg length")
plt.xlabel("msg lengths")
plt.ylabel("SNR in dB")
new, = plt.plot(msglens,snrs_new, label = "New scheme")
old, = plt.plot(msglens,snrs_old, label = "Old scheme")
plt.legend(handles = [new, old])
# plt.show()

# MEAN DIFFERENCE VS BIT DEPTH

msg =  ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=str_size))
msg = msg.encode()
bit_depths = list(range(1,9))
mean_diffs_old = []
mean_diffs_new = []

print("\nCalculating mean difference for different bit depths: ")
for i in tqdm(range(len(bit_depths))):
    _,_,mean_old = encode(msg, cover, bit_depths[i])
    snr_old = snr_analysis("cover_trim.wav","encoded.wav")
    mean_diffs_old.append(mean_old)
    _,_,mean_new = encode_new(msg, cover, bit_depths[i])
    mean_diffs_new.append(mean_new)


plt.figure(3)
plt.title("Comparison of schemes for mean difference")
plt.xlabel("bit depths")
plt.ylabel("Mean difference")
new, = plt.plot(bit_depths,mean_diffs_new, label = "New scheme")
old, = plt.plot(bit_depths,mean_diffs_old, label = "Old scheme")
plt.legend(handles = [new, old])
plt.show()


