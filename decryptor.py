from PIL import Image
import hashlib
import hash_image
import numpy as np
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
    sequence = hash_image.get_indices(key_to_int(pwd_hash.digest()), n, width, height)
    message = ''
    bits = ''
    enc_error_count = 0
    for i in range(len(sequence)):
        row = sequence[i][0]
        col = sequence[i][1]
        pixel = pixels[row][col][0]
        changed_bits = pixel%4  # last two bits
        bits += str(int(changed_bits > 1)) + str(changed_bits%2)
    for bit_idx in range(0, len(bits), 8):
        ch_bits = bits[bit_idx : bit_idx + 8]
        asc = int(ch_bits, 2)
        if asc < 128:
            message += chr(asc)
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



