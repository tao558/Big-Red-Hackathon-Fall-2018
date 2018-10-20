from PIL import Image
import numpy as np
import sys, hashlib, binascii
import hash_image as hi
import hashlib
import decryptor.py as d  #For now




def get_binary_message(message):
	message_to_base10 = list()
	for character in message:
		message_to_base10.append(ord(character))
	out_str = ""
	for i in range(len(message_to_base10)):
		out_str += '{0:08b}'.format(message_to_base10[i])

	return out_str





if __name__ == "__main__":
	h = hashlib.sha256()
	h.update(h.encone("utf-8"))
	message = sys.argv[1]
	username = sys.argv[2]
	h.update(sys.argv[3])   #This is the seed for the random number generator
	
	im = Image.open("Jake.jpg")
	im.show()



	# This gets a 3 dimensional array of RBG data.
	# First inner array is a row of pixels
	# Each array in that row represent a pixel in RBG format	
	rgb_array = np.asarray(im)



	#Vectorize numpy's function to convert to binary.
	#This is so we can efficiently convert the whole 3D array
	binary_repr_vec = np.vectorize(np.binary_repr)
	binary_array = binary_repr_vec(rgb_array)




	#Now lets work on the random number generator to get the indices of the picture to change
	#Lets also convert our message and password.
	hashed_password = h.digest()
	np.random.seed(hashed_password)
	message_bin = get_binary_message(message)
	pass_as_int = d.key_to_int(hashed_password)

	#How many random numbers do we need?
	#We need the number of bits of the message divided by 2.
	#We take the ceiling of that in case the number of bits is odd.
	num_pixels_change = len(message_bin)/2  
	#Now lets generate that many random numbers
	#Need total number of pixels
	width, height = im.size
	total_num_pixels = width * height

	#Alright now we can get the indices of the pixels to change
	indices = hi.get_indices(hashed_password, num_pixels_to_change, width, height)
