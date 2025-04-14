def min_coins(change):
    coins = [500, 100, 50, 10, 5, 1]
    count = 0
    for coin in coins:
        count += change // coin
        change %= coin
    return count

paid = int(input())
change = 1000 - paid
print(min_coins(change))
