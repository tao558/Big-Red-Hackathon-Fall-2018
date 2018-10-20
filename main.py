from PIL import Image
import numpy as np


if __name__ == "__main__":
	im = Image.open("Jake.jpg")
	im.show()

	# This gets a 3 dimensional array of RBG data.
	# First inner array is a row of pixels
	# Each array in that row represent a pixel in RBG format	
	rgb_array = np.asarray(im)
	#print(rgb_array)		

	#Vectorize numpy's function to convert to binary.
	#This is so we can efficiently convert the whole 3D array
	binary_repr_vec = np.vectorize(np.binary_repr)
	binary_array = binary_repr_vec(rgb_array)
	#print(binary_array)
