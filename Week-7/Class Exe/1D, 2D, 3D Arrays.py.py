

import numpy as np

# 1D Array
arr_1d = np.array([1, 2, 3])

# 2D Array
arr_2d = np.array([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
])

# 3D Array
arr_3d = np.array([
    [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]
    ],
    [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]
    ],
    [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]
    ]
])

print("1D Array:")
print(arr_1d)

print("\n2D Array:")
print(arr_2d)

print("\n3D Array:")
print(arr_3d)

print("\nArray Dimensions:")
print("1D array dimensions:", arr_1d.ndim)
print("2D array dimensions:", arr_2d.ndim)
print("3D array dimensions:", arr_3d.ndim)

print("\nArray Shapes:")
print("1D array shape:", arr_1d.shape)
print("2D array shape:", arr_2d.shape)
print("3D array shape:", arr_3d.shape)