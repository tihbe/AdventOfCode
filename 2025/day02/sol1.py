with open("input.txt") as f_hndl:
    data = f_hndl.read().strip().split(",")

values = [
    tuple(int(x) for x in part.split("-")) for part in data 
]
    
total = 0
for range_start, range_end in values:
    for nb in range(range_start, range_end+1):
        nb_str = str(nb)
        len_nb = len(nb_str)//2
        if nb_str[:len_nb] == nb_str[len_nb:]:
            total += nb

print(total)
