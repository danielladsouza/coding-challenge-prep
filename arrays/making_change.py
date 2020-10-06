# EPI 17.0
# Implement a greedy algorithm for making change using the min number of coins

def make_change(cents: int)->int:
    coins = [100, 50, 25, 10, 5, 1]
    num_coins = 0

    for c in coins:
        if c <= cents:
            num_coins += cents // c
            cents %= c
            if cents == 0:
                break

    return num_coins

result = make_change(500)
print(result)