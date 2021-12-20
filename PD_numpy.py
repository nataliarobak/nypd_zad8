import numpy as np
import math

arr = np.load("ex3_data.npy")
num_rows, num_cols = arr.shape
arr = arr[~np.isnan(arr)]
print("Number of rows dropped during filtration: ", num_rows - arr.num_rows)

counter = 0
for i in num_cols:
    for j in num_rows:
        if math.isnan(arr[i][j]):
            counter += 1
    print("There is ", counter, "NaN's in column ", i)

