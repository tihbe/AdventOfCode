import numpy as np

v1, v2 = np.loadtxt("input.txt").T
print(np.linalg.norm(np.sort(v1) - np.sort(v2), 1))
