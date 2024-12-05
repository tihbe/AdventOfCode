import numpy as np


def chars_to_count(char_list):
    string = "".join(char_list)
    return string.count("XMAS") + string.count("SAMX")


with open("input.txt") as f_hndl:
    mat = np.array([list(row.strip()) for row in f_hndl.readlines() if row])

cnt = 0
cnt += sum(chars_to_count(row) for row in mat)
cnt += sum(chars_to_count(col) for col in mat.T)

assert mat.shape[0] == mat.shape[1]
for k in range(-mat.shape[0], mat.shape[0]):
    cnt += chars_to_count(np.diag(mat, k))
    cnt += chars_to_count(np.diag(np.fliplr(mat), k))

print(cnt)
