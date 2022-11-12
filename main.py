from utils import *
from blowfish import *
from encoder import *

msg = "This is a sophisticated message"

key = b"this is a secret key"

bf = bf_enc(msg,key)

s_key = encode(bf.decode("unicode_escape"),r"C:\Users\amith\Code\crypto\audio-stegano-blowfish\cover.wav")

cp = decode(r"C:\Users\amith\Code\crypto\audio-stegano-blowfish\encoded.wav",s_key)

print(cp)

print(bf_dec(cp,key))
