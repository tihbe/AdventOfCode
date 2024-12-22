with open("input.txt") as f_hndl:
    initial_secrets = [int(line) for line in f_hndl.readlines()]


def get_next_secret(secret, steps):
    for i in range(steps):
        secret = ((secret * 64) ^ secret) % 16777216
        secret = ((secret // 32) ^ secret) % 16777216
        secret = ((secret * 2048) ^ secret) % 16777216
    return secret


print(sum(get_next_secret(secret, 2000) for secret in initial_secrets))
