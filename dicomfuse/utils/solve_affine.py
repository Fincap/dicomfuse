from typing import List, Tuple

import numpy as np

def __validate_points(from_points: List[Tuple[float, ...]], to_points: List[Tuple[float, ...]]):
  """
  Validates that the two list of points given are of equal length and dimensionality (i.e. they correspond).
  """
  # Check neither list is empty:
  if len(from_points) == 0 or len(to_points) == 0:
    raise Exception("Points cannot be empty.")

  # Check the lists are both the same length
  if len(from_points) != len(to_points):
    raise Exception("From and to points are not the same length.")
  
  # Check if the dimensionality is consistent throughout both lists
  primary_dimensionality = len(from_points[0])
  for p in from_points:
    if len(p) != primary_dimensionality:
      raise Exception("Inconsistent dimensionality in from points.")

  secondary_dimensionality = len(to_points[0])
  for s in to_points:
    if len(s) != secondary_dimensionality:
      raise Exception("Inconsistent dimensionality in to points.")


def get_transform_function(from_points: List[Tuple[float, ...]], to_points: List[Tuple[float, ...]]):
  """
  Calculate the affine transformation matrix from moving to fixed and return a function that applies this
  transformation to a given set of points.
  Credit to Stack Overflow user 'mathematical.coffee': https://stackoverflow.com/a/8874969 for basis of function.
  """

  try:
    __validate_points(from_points, to_points)
  except Exception as e:
    raise e

  dimensionality = len(from_points[0])

  x = np.transpose(np.matrix(from_points))
  y = np.transpose(np.matrix(to_points))

  # Add ones on the bottom of x and y
  x_one_row = [1 for i in range(len(from_points))]
  y_one_row = [1 for i in range(len(to_points))]

  x = np.vstack((x, x_one_row))
  y = np.vstack((y, y_one_row))

  # Solve for augmented matrix
  A2 = y * x.I

  # Return function that takes input x and transforms it, removing addittional row
  return lambda x: (A2 * np.vstack((np.matrix(x).reshape(dimensionality, 1), 1)))[0:dimensionality,:]
