import numpy as np

import dicomfuse

fixed_points = [
  (1, 1),
  (2, 2),
  (3, 3),
  (4, 4)
]

moving_points = [
  (1, 2),
  (2, 3),
  (3, 4),
  (4, 5)
]


t = dicomfuse.get_transform_matrix(fixed_points, moving_points)
result = dicomfuse.apply_transform_to_points(t, moving_points)
print(result)
