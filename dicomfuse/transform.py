from typing import List, Tuple

from .utils import get_transform_function

def apply_transform_to_points(from_points: List[Tuple[float, ...]], to_points: List[Tuple[float, ...]]):
  """[summary]

  Args:
      from_points (List[Tuple[float, ...]]): [description]
      to_points (List[Tuple[float, ...]]): [description]

  Returns:
      [type]: [description]
  """
  transform = get_transform_function(from_points, to_points)
  transformed_points: List[Tuple[float, ...]] = []
  
  for point in from_points:
    transformed_vector = transform(point).A1
    transformed_vector_as_tuple = (transformed_vector[0], transformed_vector[1])
    transformed_points.append(transformed_vector_as_tuple)

  return transformed_points
