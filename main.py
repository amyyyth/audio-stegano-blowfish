from utils import *
from blowfish import *
from encoder import *

msg = "Bro this is working fr fr fr"

key = b"this is a secret key or is it"

bf = bf_enc(msg,key)

s_key = encode(bf,r"C:\Users\amith\Code\crypto\audio-stegano-blowfish\cover.wav")

s_key_bf = bf_enc(str(s_key),key)

end_encoder(r"C:\Users\amith\Code\crypto\audio-stegano-blowfish\encoded.wav",s_key_bf)

s_key_rec = end_decoder(r"C:\Users\amith\Code\crypto\audio-stegano-blowfish\encoded.wav")

s_key_dec = bf_dec(s_key_rec,key)

cp = decode(r"C:\Users\amith\Code\crypto\audio-stegano-blowfish\encoded.wav",(s_key_dec))

msg_rec = (bf_dec(cp,key))

print(msg_rec)
