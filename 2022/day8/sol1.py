import numpy as np

with open("input.txt", "r") as f_hndl:
    forest = []
    for line in f_hndl:
        forest.append([int(tree) for tree in line.rstrip()])
    forest = np.array(forest)

    # Accumulate max in every direction
    max_x1 = np.maximum.accumulate(forest, axis=0)
    max_x2 = np.maximum.accumulate(forest[::-1], axis=0)
    max_y1 = np.maximum.accumulate(forest, axis=1)
    max_y2 = np.maximum.accumulate(forest[:, ::-1], axis=1)

    # Compute diffs in every direction
    diff_x1 = np.diff(max_x1, axis=0, prepend=-1)
    diff_x2 = np.diff(max_x2, axis=0, prepend=-1)[::-1]
    diff_y1 = np.diff(max_y1, axis=1, prepend=-1)
    diff_y2 = np.diff(max_y2, axis=1, prepend=-1)[:, ::-1]

    # Compute mask of visible trees
    visible_trees = (diff_x1 > 0) | (diff_x2 > 0) | (diff_y1 > 0) | (diff_y2 > 0)
    visible_trees_count = np.count_nonzero(visible_trees)

    print(visible_trees_count)
