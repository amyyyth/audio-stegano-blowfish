from utils import *
from blowfish import *
from encoder import *
import string 
import random

print("------------ Sender ------------ ")
# msg = "Location of the secret safe house: 11.268501570832086, 75.79267392030299"
# msg = "sh"
msg =  ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=15000))
print("Message: ",msg)
max_bit_depth = 4

key = b"thisisasecretkey"

bf = bf_enc(msg,key)
print("\nBlowfish encrypted message: ",bf)

# s_key,_ ,_ = encode(bf,r"cover_trim.wav", max_bit_depth,"encoded.wav")
s_key,_ ,_ = encode_new(bf,r"cover_trim.wav", max_bit_depth,"encoded.wav")

print("\nSymmetric key of encoder: ", s_key)
s_key_bf = bf_enc(str(s_key),key)
print("\nEncrypted symmetric key of encoder: ", s_key_bf)

end_encoder(r"encoded.wav",s_key_bf,"encoded.wav")

print("\n\n------------ Receiver ------------ ")

s_key_rec = end_decoder(r"encoded.wav")
print("Recovered encrypted symmetric key of encoder: ", s_key_rec)

s_key_dec = bf_dec(s_key_rec,key)
print("\nDecrypted symmetric key of encoder: ", s_key_dec)

cp = decode(r"encoded.wav", max_bit_depth,(s_key_dec))

print("\nRecovered message from audio: ", cp)
msg_rec = (bf_dec(cp,key))

print("\nDecrypted message: ", msg_rec)
print("\n\n\n")
# print(msg_rec)

# print(msg_rec == msg)

