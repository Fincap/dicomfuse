import numpy as np

from dicomfuse import apply_transform_to_points

primary_points = [
  (1, 1),
  (2, 2),
  (3, 3),
  (4, 4)
]

secondary_points = [
  (1, 2),
  (2, 3),
  (3, 4),
  (4, 5)
]


result = apply_transform_to_points(primary_points, secondary_points)
print(result)
