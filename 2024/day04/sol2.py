import numpy as np


def valid_mas(char_list):
    return "".join(char_list) in ("MAS", "SAM")


with open("input.txt") as f_hndl:
    mat = np.array([list(row.strip()) for row in f_hndl.readlines() if row])

cnt = 0
for i in range(mat.shape[0] - 2):
    for j in range(mat.shape[1] - 2):
        diag1 = (mat[i, j], mat[i + 1, j + 1], mat[i + 2, j + 2])
        diag2 = (mat[i + 2, j], mat[i + 1, j + 1], mat[i, j + 2])
        cnt += valid_mas(diag1) and valid_mas(diag2)

print(cnt)
