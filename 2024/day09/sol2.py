with open("input.txt") as f_hndl:
    disk_map = f_hndl.readline().strip()

# Create disk map with ids
disk_map_with_ids = []
data_cntr = 0

for p, count in enumerate(disk_map):
    is_data = p % 2 == 0
    disk_map_with_ids.append((data_cntr if is_data else -1, int(count)))
    data_cntr += is_data

# Optimize disk map with new strategy
while True:
    left_ptr = 0
    right_ptr = len(disk_map_with_ids) - 1
    while left_ptr < right_ptr:
        id_l, cnt_l = disk_map_with_ids[left_ptr]
        if id_l != -1:
            left_ptr += 1
            continue
        id_r, cnt_r = disk_map_with_ids[right_ptr]
        if id_r == -1:
            right_ptr -= 1
            continue

        if cnt_r == cnt_l:  # same size, move right to left
            disk_map_with_ids[left_ptr] = id_r, cnt_r
            disk_map_with_ids[right_ptr] = -1, cnt_r
            break
        elif cnt_r < cnt_l:  # right fit in left, insert
            disk_map_with_ids[left_ptr] = -1, cnt_l - cnt_r
            disk_map_with_ids[right_ptr] = -1, cnt_r
            disk_map_with_ids.insert(left_ptr, (id_r, cnt_r))
            break
        else:  # doesn't fit
            right_ptr -= 1
    else:
        id_l, cnt_l = disk_map_with_ids[left_ptr]
        if id_l == -1:  # size could be too small, skip this free space
            disk_map_with_ids[left_ptr] = -2, cnt_l
        else:  # everything is full
            break


# Compute output
checksum = 0
pos = 0
for id, size in disk_map_with_ids:
    if id > 0:
        checksum += id * size * (pos + size / 2 - 1 / 2)
        # same as sum(id * s for s in range(pos, pos + size))
    pos += size
print(checksum)
