import numpy as np
import scipy.misc as misc

def visualize_digits(matrix, count, row_count, col_count):
  pass


if __name__ == '__main__':
  # load training data
  digits = np.loadtxt('data/train2.csv', delimiter = ',')
  labels = digits[:,0]
  # each image is a 28 x 28
  pixels = digits[:,1:]
  

  import pdb; pdb.set_trace()
