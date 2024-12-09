with open("input.txt") as f_hndl:
    disk_map = f_hndl.readline().strip()

# Create disk from disk map
disk = []
data_cntr = 0

for p, char in enumerate(disk_map):
    is_data = p % 2 == 0
    for _ in range(int(char)):
        disk.append(data_cntr if is_data else -1)
    data_cntr += is_data

# Optimize disk from strategy
left_ptr = 0
right_ptr = len(disk) - 1

while left_ptr != right_ptr:
    if disk[left_ptr] != -1:
        left_ptr += 1
        continue
    disk[left_ptr] = disk[right_ptr]
    disk[right_ptr] = -1
    right_ptr -= 1

# Compute output
checksum = sum(pos * val for pos, val in enumerate(disk) if val != -1)
print(checksum)
