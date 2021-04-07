import numpy as np

from dicomfuse.utils import get_transform_function

primary_points = [
  (1, 1),
  (2, 2),
  (3, 3),
  (4, 4)
]

secondary_points = [
  (1, 2.1),
  (2.8, 3.2),
  (3, 4.3),
  (4, 5.4)
]


transform_function = get_transform_function(primary_points, secondary_points)

result = transform_function(primary_points[1])
print(result)
