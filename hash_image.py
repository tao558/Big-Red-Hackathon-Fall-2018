import numpy as np


#Seed is the seed for the RNG
#n is the number of pixels to change
#p_row is the number of pixels per row
#p_col is the number of pixels per column
def get_indices(seed, n, p_row, p_col):
    p_total = p_row*p_col
    if (n > p_total):
        raise RuntimeError("Number of pixels to change must be <= total number of pixels")
    np.random.seed(seed)
    ans = list()
    for i in range(n):
        row = np.random.randint(0, p_col)
        col = np.random.randint(0, p_row)
        coords = (row, col)
        ans.append(coords)
    return ans
