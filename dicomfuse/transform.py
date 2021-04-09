from typing import List, Tuple

import numpy as np


def __validate_points(fixed_points: List[Tuple[float, ...]], moving_points: List[Tuple[float, ...]]):
  """
  Validates that the two list of points given are of equal length and dimensionality (i.e. they correspond).
  """
  # Check neither list is empty:
  if len(moving_points) == 0 or len(fixed_points) == 0:
    raise Exception("Points cannot be empty.")

  # Check the lists are both the same length
  if len(moving_points) != len(fixed_points):
    raise Exception("From and to points are not the same length.")
  
  # Check if the dimensionality is consistent throughout both lists
  primary_dimensionality = len(moving_points[0])
  for p in moving_points:
    if len(p) != primary_dimensionality:
      raise Exception("Inconsistent dimensionality in moving points.")

  secondary_dimensionality = len(fixed_points[0])
  for s in fixed_points:
    if len(s) != secondary_dimensionality:
      raise Exception("Inconsistent dimensionality in fixed points.")


def get_transform_matrix(fixed_points: List[Tuple[float, ...]], moving_points: List[Tuple[float, ...]]):
  """
  Calculate the affine transformation matrix from moving to fixed, given that moving_points is a known transformation
  of fixed_points. 
  Credit to Stack Overflow user 'mathematical.coffee': https://stackoverflow.com/a/8874969 for basis of function.
  """

  try:
    __validate_points(fixed_points, moving_points)
  except Exception as e:
    raise e

  fixed_matrix = np.transpose(np.matrix(fixed_points))
  moving_matrix = np.transpose(np.matrix(moving_points))

  # Augment '1' at the end of all vectors
  augment_row = [1 for i in range(len(moving_points))]
  fixed_matrix = np.vstack((fixed_matrix, augment_row))
  moving_matrix = np.vstack((moving_matrix, augment_row))

  # Solve for augmented matrix
  transformation_matrix = fixed_matrix * moving_matrix.I

  return transformation_matrix

  # TODO split this up into two functions: get transformation matrix (A2) and apply matrix to vector.
  # Also should probably rename 'x' and 'y' to something more descriptive such as original_points and
  # known_transformed_points.

  # Return function that takes input x and transforms it, removing addittional row
  # return lambda x: (A2 * np.vstack((np.matrix(from_matrix).reshape(dimensionality, 1), 1)))[0:dimensionality,:]



def apply_transform_to_points(transformation_matrix: np.matrix, moving_points: List[Tuple[float, ...]]):
  """Apply the transformation matrix to a set of moving points and return the the transformed moving points.

  Args:
      transformation_matrix (np.matrix): Affine transformation matrix.
      moving_points (List[Tuple[float, ...]]): The set of points to be transformed.
  """

  dimensionality = len(moving_points[0])

  moving_matrix = np.transpose(np.matrix(moving_points))
  augment_row = [1 for i in range(len(moving_points))]
  moving_matrix = np.vstack((moving_matrix, augment_row))

  transformed_matrix = (transformation_matrix * moving_matrix)[0:dimensionality,:].T
  transformed_points = [tuple(row.tolist()[0]) for row in transformed_matrix]

  return transformed_points
