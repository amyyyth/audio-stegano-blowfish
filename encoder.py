from utils import *
from adjustment import *

    

def encode_new(msg,cover,out_file):

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
        dec_val = audio[s]
        val = bin(audio[s])[2:]
        val = ('0'*(8-len(val)))+val

        if q == 0:
            q = 1

        if(val[-q] != b_enc[i]):
            ad_val = adjust(dec_val,q,b_enc[i])
            # print("b = ",b_enc[i],"q = ",q," ",dec_val,"-->",ad_val,bin(dec_val)[2:],"-->",bin(ad_val)[2:])
            audio[s] = ad_val

        s += q
        t = sum_digits(s)
        q = t % 8

    # WRITE INTO AUDIO FILE
    with open('encoded.wav', mode='bw+') as f:
        f.write(audio)
    
    return s_key



def encode(msg,cover,out_file):

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



msg = b"sed euismod nisi porta lorem mollis aliquam ut porttitor leo a diam sollicitudin tempor id eu nisl nunc mi ipsum faucibus vitae aliquet nec ullamcorper sit amet risus nullam eget felis eget nunc lobortis mattis aliquam faucibus purus in massa tempor nec feugiat nisl pretium fusce id velit ut tortor pretium viverra suspendisse potenti nullam ac tortor vitae purus faucibus ornare suspendisse sed nisi lacus sed viverra tellus in hac habitasse platea dictumst vestibulum rhoncus est pellentesque elit ullamcorper dignissim cras tincidunt lobortis feugiat vivamus at augue eget arcu dictum varius duis at consectetur lorem donec massa sapien faucibus et molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed ullamcorper morbi tincidunt ornare massa eget egestas purus viverra accumsan in nisl nisi scelerisque eu ultrices vitae auctor eu augue ut lectus arcu bibendum at varius vel pharetra vel turpis nunc eget lorem dolor sed viverra ipsum nunc aliquet bibendum enim facilisis gravida neque convallis a cras semper auctor neque vitae tempus quam pellentesque nec nam aliquam sem et tortor consequat id porta nibh venenatis cras sed felis eget velit aliquet sagittis id consectetur purus ut faucibus pulvinar elementum integer enim neque volutpat ac tincidunt vitae semper quis lectus nulla at volutpat diam ut venenatis tellus in metus vulputate eu scelerisque felis imperdiet proin fermentum leo vel orci porta non pulvinar neque laoreet suspendisse interdum consectetur libero id faucibus nisl tincidunt eget nullam non nisi est sit amet facilisis magna etiam tempor orci eu lobortis elementum nibh tellus molestie nunc non blandit massa enim nec dui nunc mattis enim ut tellus elementum sagittis vitae et leo duis ut diam quam nulla porttitor massa id neque aliquam vestibulum morbi blandit cursus risus at ultrices mi tempus imperdiet nulla malesuada pellentesque elit eget gravida cum sociis natoque penatibus et magnis dis parturient montes nascetur ridiculus mus mauris vitae ultricies leo integer malesuada nunc vel risus commodo viverra maecenas accumsan lacus vel facilisis volutpat est velit egestas dui id ornare arcu odio ut sem nulla pharetra diam sit amet nisl suscipit adipiscing bibendum est ultricies integer quis auctor elit sed vulputate mi sit amet mauris commodo quis imperdiet massa tincidunt nunc pulvinar sapien et ligula ullamcorper malesuada proin libero nunc consequat interdum varius sit amet mattis vulputate enim nulla aliquet porttitor lacus luctus accumsan tortor posuere ac ut consequat"


s_key = encode_new(msg,r"cover.wav","encoded_new.wav")

s_key = encode(msg,r"cover.wav","encoded_old.wav")
