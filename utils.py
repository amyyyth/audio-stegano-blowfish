
def read_audio(file):
    with open(file, 'rb') as fd:
        contents = fd.read()
    return bytearray(contents);

def sum_digits(n):
     
    strr = str(n)
    list_of_number = list(map(int, strr.strip()))
    return sum(list_of_number)

def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')

def binstream_to_bin(b):
    bs = ''
    for i in range(len(b)):
        byt = bin((b[i]))[2:]
        byt = ('0'*(8-len(byt)))+byt
        bs+=byt
    return bs

def bin_to_binstream(bs):
    dec = bytearray()
    for i in range(0,len(bs),8):
        dec.append(int(bs[i:i+8],2))
    return dec
