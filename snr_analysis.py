import numpy as np
from encoder import *
from blowfish import *
from utils import *



def snr_analysis(original_file, encoded_file):
    # original_file = r"cover_trim.wav"
    # encoded_file = r"encoded.wav"
    original_audio = read_audio(original_file)
    encoded_audio = read_audio(encoded_file)

    noise_pwr = 0
    sig_pwr = 0

    for i in range(len(original_audio)):
        sig_pwr += (original_audio[i]**2)
        noise_pwr += ((original_audio[i] - encoded_audio[i])**2)

    snr = 10*(np.log10(sig_pwr/noise_pwr))

    return snr