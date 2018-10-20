from PIL import Image
import hashlib
import ./hash
def decrypt(directory, pwd):
    """
    This function will decrypt a message inside an image.
    :var directory: string ~ file path to image
    :var pwd: string ~ password used to retrieve encryption. 
    """

    pwd_hash = hashlib.sha256()
    pwd_hash.update(pwd.encode('utf-8'))
    orig_im = Image.open(directory)
    pixels = list(orig_im.getdata())
    width, height = orig_im.size
    pixels = [pixels[i * width : (i+1) * width] for i in range(height)]
    sequence = get_indices(pwd)
    message = ''
    for i in range(len(sequence)):
        row = sequence[i][0]
        col = sequence[i][1]
        pixel = pixels[row][col][i%3]
        pixel = int(pixel, 2)


