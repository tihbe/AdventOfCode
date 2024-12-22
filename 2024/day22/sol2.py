from collections import defaultdict, deque


with open("input.txt") as f_hndl:
    initial_secrets = [int(line) for line in f_hndl.readlines()]


max_bananas = defaultdict(int)

for secret in initial_secrets:
    sequences_for_secret = {}
    price_diff = deque([], maxlen=4)
    previous_banana_price = None

    for i in range(2000):
        secret = ((secret * 64) ^ secret) % 16777216
        secret = ((secret // 32) ^ secret) % 16777216
        secret = ((secret * 2048) ^ secret) % 16777216
        banana_price = secret % 10
        if previous_banana_price is not None:
            price_diff.append(banana_price - previous_banana_price)
        previous_banana_price = banana_price

        if len(price_diff) == 4:
            tpl = tuple(price_diff)
            if tpl not in sequences_for_secret:
                sequences_for_secret[tpl] = banana_price

    for price_diff, price in sequences_for_secret.items():
        max_bananas[price_diff] += price

print(max(max_bananas.values()))
