with open("input.txt", "r") as f_hndl:
    payload = f_hndl.read().rstrip()
    for i in range(len(payload)):
        subset = payload[i : i + 14]
        if len(set(subset)) == len(subset):
            print(i + 14)
            break
