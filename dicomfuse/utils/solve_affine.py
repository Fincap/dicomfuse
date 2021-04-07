from typing import List, Tuple

import numpy as np

def _validate_points(primary_points: List[Tuple[float, float]], secondary_points: List[Tuple[float, float]]):
  """
  Validates that the two list of points given are of equal length and dimensionality (i.e. they correspond).
  """
  # Check neither list is empty:
  if len(primary_points) == 0 or len(secondary_points) == 0:
    raise Exception("Points cannot be empty.")

  # Check the lists are both the same length
  if len(primary_points) != len(secondary_points):
    raise Exception("Primary and secondary points are not the same length.")
  
  # Check if the dimensionality is consistent throughout both lists
  primary_dimensionality = len(primary_points[0])
  for p in primary_points:
    if len(p) != primary_dimensionality:
      raise Exception("Inconsistent dimensionality in primary points.")

  secondary_dimensionality = len(secondary_points[0])
  for s in secondary_points:
    if len(s) != secondary_dimensionality:
      raise Exception("Inconsistent dimensionality in secondary points.")


def get_transform_function(primary_points: List[Tuple[float, float]], secondary_points: List[Tuple[float, float]]):
  """
  Calculate the affine transformation matrix from primary to secondary and return a function that applies this
  transformation to the given set of points.
  Credit to Stack Overflow user 'mathematical.coffee': https://stackoverflow.com/a/8874969 for basis of function.
  """

  try:
    _validate_points(primary_points, secondary_points)
  except Exception as e:
    raise e

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
