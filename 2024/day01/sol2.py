from collections import Counter
import numpy as np

v1, v2 = np.loadtxt("input.txt").T

cnt = Counter(v2)
print(sum(v * cnt.get(v, 0) for v in v1))
