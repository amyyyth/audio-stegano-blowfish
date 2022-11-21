from utils import *

def encode(msg,cover):

    # READ AUDIO
    audio = read_audio(cover)

    # ENCODE THE MSG
    b_enc = binstream_to_bin(msg)

    msg_len = len(b_enc)//8

    # COMPUTING THE FIRST LOCATION TO HIDE
    s = msg_len + 60         # Leave space for the header of the file to remain unchanged
    t = sum_digits(s)
    q = t % 8

    # FIRST LOCATION TO HIDE IS THE KEY
    s_key = s

    # ENCODE THE REST
    for i in range(len(b_enc)):
        val = bin(audio[s])[2:]
        val = ('0'*(8-len(val)))+val
        if q == 0 or q == 1:
            q = 1
            val = val[:-1] + b_enc[i]
        else:
            val = val[:-q] + b_enc[i] + val[-q+1:]

        audio[s] = int(val,2)
        s += q
        t = sum_digits(s)
        q = t % 8

    # WRITE INTO AUDIO FILE
    with open('encoded.wav', mode='bw+') as f:
        f.write(audio)
    
    return s_key


def decode(file,s_key):

    # READ AUDIO
    audio = read_audio(file)

    s = s_key        # Get the first hidden position
    t = sum_digits(s)
    q = t % 8
    s = int(s)
    l = 8*(s - 60)

    b = ''

    for i in range(l):
        byt = bin(audio[s])[2:]
        byt = ('0'*(8 - len(byt)))+byt
        if(q == 0):
            q = 1
        b += byt[-q]
        s += q
        t = sum_digits(s)
        q = t % 8

    return bin_to_binstream(b)


def end_encoder(cover, byts):
    # READ AUDIO
    audio = read_audio(cover)

    # ENCODE THE MSG
    b_enc = binstream_to_bin(byts)
    j = 0

    for i in range(len(audio)-1,len(audio)-len(b_enc)-1,-1):
        # print(audio[i],"->",b_enc[len(audio)-i -1])
        val = bin(audio[i])[2:]
        val = ('0'*(8-len(val)))+val
        val = val[:-2]+'0'+ b_enc[j]    # '0' TO know that there is more data to decode
        audio[i] = int(val,2)
        j+=1

    # for i in range(len(audio)-1,len(audio)-len(b_enc),-1):
    #     val = bin(audio[i])[2:]
    #     val = ('0'*(8-len(val)))+val
    #     val = val[:-2]+'0'+ b_enc[j]    # '0' TO know that there is more data to decode
    #     audio[i] = int(val,2)

    eod_marker_pos = -(len(b_enc)+1)

    val = bin(audio[eod_marker_pos])[2:]
    val = ('0'*(8-len(val)))+val
    val = val[:-2]+'1'+val[-1]
    audio[eod_marker_pos] = int(val,2)     # Mark the end of data

    # WRITE INTO AUDIO FILE
    with open('encoded.wav', mode='bw+') as f:
        f.write(audio)

def end_decoder(aud):
    # READ AUDIO
    audio = read_audio(aud)
    s = ''
    for i in range(len(audio)-1,-1,-1):
        val = bin(audio[i])[2:]
        val = ('0'*(8-len(val)))+val
        if(val[-2] == '1'):
            break
        s += val[-1]

    return bin_to_binstream(s)


