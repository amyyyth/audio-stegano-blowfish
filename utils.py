
def read_audio(file):
    with open(file, 'rb') as fd:
        contents = fd.read()
    return bytearray(contents);


def str_to_bin(msg):
    b_enc = ''
    for x in msg:
        b = format(ord(x), 'b')
        b = '0'*(8-len(b))+b
        b_enc += b
    return b_enc

def bin_to_str(b_enc):
    dec = ''
    for i in range(0,len(b_enc),8):
        dec += chr(int(b_enc[i:i+8],2))
    return dec


def sum_digits(n):
     
    strr = str(n)
    list_of_number = list(map(int, strr.strip()))
    return sum(list_of_number)
