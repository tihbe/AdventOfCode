import re
from pathlib import Path
from collections import defaultdict

with open("input.txt", "r") as f_hndl:
    current_path = Path("/")
    file_sizes_sum = defaultdict(int)
    command_regex = re.compile("\$ (cd|ls)\s*(.*)")
    ls_regex = re.compile("(dir|[0-9]+)\s+(.+)")
    for line in f_hndl:
        line = line.rstrip()
        if reg_match := command_regex.match(line):
            command = reg_match.group(1)
            if command == "cd":
                next_path = reg_match.group(2)
                if next_path.startswith("/"):
                    current_path = Path(next_path)
                elif next_path == "..":
                    current_path = current_path.parent
                else:
                    current_path = current_path / next_path
            elif command == "ls":
                continue
        else:  # Assumes ls output
            if reg_match := ls_regex.match(line):
                if reg_match.group(1) == "dir":
                    continue
                else:
                    file_size = int(reg_match.group(1))
                    file_name = reg_match.group(2)
                    temp_path = current_path
                    file_sizes_sum[str(temp_path)] += file_size

                    while str(temp_path) != temp_path.root:
                        temp_path = temp_path.parent
                        file_sizes_sum[str(temp_path)] += file_size

    used_disk_space = file_sizes_sum[current_path.root]
    unused_disk_space = 70_000_000 - used_disk_space
    needed_disk_space = 30_000_000 - unused_disk_space
    deleted_folder_size = min(
        directory_sum for directory_sum in file_sizes_sum.values() if directory_sum >= needed_disk_space
    )

    print(deleted_folder_size)
