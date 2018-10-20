import numpy as np


#Seed is the seed for the RNG
#n is the number of pixels to change
#t is the total number of pixels
def get_indices(seed, n, t):
	if (n > t):
		raise RuntimeError("Number of pixels to change must be <= total number of pixels")
	np.random.seed(seed)
	ans = list()
	for i in range(n):
		row = np.random.randint(0, t)
		col = np.random.randint(0, t)
		coords = (row, col)
		ans.append(coords)
	return ans