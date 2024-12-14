import re
import numpy as np
import cv2
from PIL import Image

width = 101
height = 103

with open("input.txt") as f_hndl:
    positions = re.findall("p=(\d+),(\d+) v=(-?\d+),(-?\d+)", f_hndl.read())


duration = 0
last_entropy = None
while True:
    mat = np.zeros((width, height))
    for guard in positions:
        x, y, vx, vy = map(int, guard)
        fx = (x + vx * duration) % width
        fy = (y + vy * duration) % height
        mat[fx, fy] += 1
    duration += 1

    img = Image.fromarray(mat)
    new_entropy = img.entropy()
    if last_entropy is None:
        last_entropy = new_entropy
    diff = abs(last_entropy - new_entropy)

    if duration % 100 == 0:
        print(f"Step : {duration}")

    if diff < 0.001:
        continue

    try:
        cv2.imshow("Is this a christmas tree?", mat)
        k = cv2.waitKey(1000)
        if k == ord(" "):  # space bar
            print(duration - 1)
            break
    except:
        cv2.destroyAllWindows()
        break
