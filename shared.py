import numpy as np



def key_to_int(key):
    key = key.decode('utf-8', 'backslashreplace')
    st = ""
    for ch in key:
        st += str(ord(ch))
    return int(st)%(2**32-1)



#Seed is the seed for the RNG
#n is the number of pixels to change
#p_row is the number of pixels per row
#p_col is the number of pixels per column
def get_start_index(seed, p_row, p_col):
    p_total = p_row*p_col
    start = key_to_int(seed)%p_total
    start_col = start%p_row
    start_row = int(start/p_col)
    return (row, col)
