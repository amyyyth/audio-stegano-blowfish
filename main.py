from utils import *
from blowfish import *
from encoder import *

msg = "This is a sophisticated message or is it"

key = b"this is a secret key or is it"

bf = bf_enc(msg,key)

s_key = encode(bf,r"C:\Users\amith\Code\crypto\audio-stegano-blowfish\cover.wav")

s_key_bf = bf_enc(str(s_key),key)

end_encoder(r"C:\Users\amith\Code\crypto\audio-stegano-blowfish\cover.wav",s_key_bf)

s_key_dec = end_decoder(r"C:\Users\amith\Code\crypto\audio-stegano-blowfish\cover.wav")

cp = decode(r"C:\Users\amith\Code\crypto\audio-stegano-blowfish\encoded.wav",s_key_dec)

print(bf_dec(cp,key))
