from PIL import Image
import hashlib
import shared
import numpy as np
import encryptor as e
def decrypt(directory, pwd, n):
    """
    This function will decrypt a message inside an image.
    :var directory: string ~ file path to image
    :var pwd: string ~ password used to retrieve encryption.
    :var n: integer ~ number of pixels being altered
    :return message: string ~ hidden message decrypted from image
    This function will be updated to remove n from list of params
    """
    pwd_hash = hashlib.sha256()
    pwd_hash.update(pwd.encode('utf-8'))
    orig_im = Image.open(directory)
    pixels = list(orig_im.getdata())
    width, height = orig_im.size
    pixels = [pixels[i * width : (i+1) * width] for i in range(height)]
    seq_start_row, seq_start_col = 
    shared.get_start_index(shared.key_to_int(pwd_hash.digest()), width, height)
    length_bin = ''
    for idx in range(12):  # set length
        curr_row = seq_start_row + int((seq_start_col + idx)/width)
        curr_col = (seq_start_col + idx)%width
        if curr_row >= height:
            curr_row = 0
        pixel = pixels[curr_row][curr_col][0]  # component color value
        length_bin += last_two_bits(pixel)
        if idx == 11:  # update the starting row for rest of message
            seq_start_row = curr_row
            seq_start_col = curr_col
    message_length = int(length_bin, 2)  # number of bits
    message = ''
    bits = ''
    enc_error_count = 0
    for i in range(message_length/2):  # number of pixels
        row = seq_start_row + int((seq_start_col + i)/width)
        col = (seq_start_col + i)%width
        if curr_row >= height:
            curr_row = 0
        pixel = pixels[row][col][0]
        bits += last_two_bits(pixel)  # bits of message
    for bit_idx in range(0, len(bits), 8):
        ch_bits = bits[bit_idx : bit_idx + 8]
        asc = int(ch_bits, 2)  # bits to ascii value
        if asc < 128:
            message += chr(asc)  # ascii value to char
        else:
            enc_error_count += 1
    if enc_error_count > 0:
        print("There were", enc_error_count, "encoding errors.")
        print("Output may not return expected result")
    return message


def key_to_int(key):
    """
    This function will take a string as an input and return
    a nearly unique integer
    """
    key = key.decode('utf-8', 'backslashreplace')
    st = ""
    for ch in key:
        st += str(ord(ch))
    return int(st)%(2**32-1)

def last_two_bits(dec_num):
    dec_num = dec_num%4
    return str(int(dec_num > 1)) + str(dec_num%2)
