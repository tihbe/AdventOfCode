import numpy as np

with open("input.txt", "r") as f_hndl:
    forest = []
    for line in f_hndl:
        forest.append([int(tree) for tree in line.rstrip()])
    forest = np.array(forest)
    maximum_score = 0

    for x in range(len(forest)):
        for y in range(len(forest[0])):
            score = [0] * 4
            for dx1 in range(x - 1, -1, -1):
                score[0] += 1
                if forest[dx1, y] >= forest[x, y]:
                    break
            for dx2 in range(x + 1, len(forest)):
                score[1] += 1
                if forest[dx2, y] >= forest[x, y]:
                    break
            for dy1 in range(y - 1, -1, -1):
                score[2] += 1
                if forest[x, dy1] >= forest[x, y]:
                    break
            for dy2 in range(y + 1, len(forest[0])):
                score[3] += 1
                if forest[x, dy2] >= forest[x, y]:
                    break

            score = np.prod(score)
            maximum_score = max(score, maximum_score)

    print(maximum_score)
