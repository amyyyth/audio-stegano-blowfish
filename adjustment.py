
import math



def adjust(n, change_bit, val):
    val = str(val)
    b = bin(n)[2:]

    b = ('0'*(8-len(b)))+b


    # FORWARD
    f_val = math.inf
    b_val = math.inf
    for i in range(n+1,256):
        b_i = bin(i)[2:]
        b_i = ('0'*(8-len(b_i)))+b_i
        if(b_i[-change_bit] == val):
            f_val = i
            break

    # BACKWARD
    for i in range(n-1,-1,-1):
        b_i = bin(i)[2:]
        b_i = ('0'*(8-len(b_i)))+b_i
        if(b_i[-change_bit] == val):
            b_val = i
            break


    return f_val if min(abs(f_val - n),abs(b_val - n)) == (f_val - n) else b_val

