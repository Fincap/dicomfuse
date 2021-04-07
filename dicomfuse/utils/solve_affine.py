from typing import List, Tuple

import numpy as np


def get_transform_function(primary_points: List[Tuple[float, float]], secondary_points: List[Tuple[float, float]]):

  """Calculate the affine transformation matrix from primary to secondary and return a function that applies this
  transformation to the given set of points.
  Credit to Stack Overflow user 'mathematical.coffee': https://stackoverflow.com/a/8874969 for basis of function.
  """
  dimensionality = len(primary_points[0])

  x = np.transpose(np.matrix(primary_points))
  y = np.transpose(np.matrix(secondary_points))

  # Add ones on the bottom of x and y
  x_one_row = [1 for i in range(len(primary_points))]
  y_one_row = [1 for i in range(len(secondary_points))]

  x = np.vstack((x, x_one_row))
  y = np.vstack((y, y_one_row))

  # Solve for augmented matrix
  A2 = y * x.I

  # Return function that takes input x and transforms it, removing addittional row
  return lambda x: (A2 * np.vstack((np.matrix(x).reshape(dimensionality, 1), 1)))[0:dimensionality,:]
