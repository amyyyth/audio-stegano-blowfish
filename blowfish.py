from Crypto.Cipher import Blowfish
from struct import pack

# MSG MUST BE A STRING
def bf_enc(msg,key):
    if(type(msg) != bytes):
        encoded=msg.encode('utf-8')
        msg = bytearray(encoded)
    if(type(key) != bytes):
        encoded=key.encode('utf-8')
        key = bytearray(encoded)
    bs = Blowfish.block_size
    cipher = Blowfish.new(key, Blowfish.MODE_CBC)

    plen = bs - len(msg) % bs
    padding = [plen]*plen
    padding = pack('b'*plen, *padding)
    c_text = cipher.iv + cipher.encrypt(msg + padding)
    return c_text

# CTEXT MUST BE A BYTE ARRAY
def bf_dec(c_text,key):
    bs = Blowfish.block_size
    iv = c_text[:bs]
    c_text = c_text[bs:]

    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    msg = cipher.decrypt(c_text)

    last_byte = msg[-1]
    msg = msg[:- (last_byte if type(last_byte) is int else ord(last_byte))]
    return msg.decode(encoding="unicode_escape")

key = b"this is a big stuff that is important"


