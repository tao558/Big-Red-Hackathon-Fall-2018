from PIL import Image, ImageChops
import numpy as np
import sys, hashlib, binascii
import shared
import hashlib


MAX_BITS_MESSAGE = 12


def encode_length_and_message(message):
	message_to_base10 = list()
	out_str = ""
	for character in message:
		message_to_base10.append(ord(character))
	for i in range(len(message_to_base10)):
		out_str += '{0:08b}'.format(message_to_base10[i])

	num_pixels_changed = int(len(out_str)/2)
	out_str = np.binary_repr(num_pixels_changed, MAX_BITS_MESSAGE) + out_str
	return out_str




def alter_picture(picture, starting_index, message_bin, width, height):
	altered_picture_list = picture.copy()
	message_bin = list(message_bin)  #Convert to a list to use pop()
	(curr_row, curr_col) = starting_index
	while(len(message_bin) != 0):
		first_bit = message_bin.pop(0)
		second_bit = message_bin.pop(0)
		which_rgb = 0
		original_bin = np.binary_repr(altered_picture_list[curr_row][curr_col][which_rgb], 8)
		altered_bin = original_bin[:-2] + first_bit + second_bit
		altered_picture_list[curr_row][curr_col][which_rgb] = int(altered_bin, 2)
		#Now update the row and column
		curr_col += 1
		if (curr_col >= width):
			curr_col = 0
			curr_row += 1
		if (curr_row >= height):
			height = 0



	return Image.fromarray(altered_picture_list, 'RGB')




def encrypt():
	h = hashlib.sha256()
	message = input("What is your message?: ")
	picture_filename = input("What is the name of the picture?: ")
	#username = input("What is your username?: ")
	password = input("What is the password?: ")  #This is the seed for the random number generator
	h.update(password.encode('utf-8'))
	original_im = Image.open(picture_filename)
	


	# This gets a 3 dimensional array of RBG data.
	# First inner array is a row of pixels
	# Each array in that row represent a pixel in RBG format	
	rgb_array = np.asarray(original_im)

	#Now lets work on the random number generator to get the indices of the picture to change
	#Lets also convert our message and password.
	seed = shared.key_to_int(h.digest())

	length_and_message_bin = encode_length_and_message(message)

	#How many random numbers do we need?
	#We need the number of bits of the message divided by 2.

	#Now lets generate that many random numbers
	#Need total number of pixels
	width, height = original_im.size
	total_num_pixels = width * height
	starting_point = (seed % height, seed % width)    #This is our starting point. We start looking/encoding here, then move linearly

	#Alright now we can get the indices of the pixels to change
	starting_index = shared.get_start_index(seed, width, height)



	altered_im = alter_picture(rgb_array, starting_index, length_and_message_bin, width, height)

	#Now lets save our new image
	altered_im_filename = "stego_" + picture_filename.rsplit(".", 1)[0] + ".png"
	altered_im.save(altered_im_filename)
	altered_im.show()

	print("Encoded image saved to current directory. Titled 'stego_' then the rest of the original pictures name")
	#difference.show()
	#Alright so maybe implement the difference function. Make this run as an exe so other people
	#can easily run it. Also, implement some kind of functionality where user is asked repeatedly for
	#This password, name of the image, and their message.

encrypt()
