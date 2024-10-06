def coin_change(coins, amount):
    memo = {}
    def helper(x):
        if x <0:
            return float('inf')
        
        if x == 0:
            return 0
        
        if x in memo:
            return memo[x]
        
        min_coins = float('inf')

        for coin in coins:
            result = helper(x - coin)
            if result != float('inf'):
                min_coins = min(min_coins, result + 1)
        memo[x] = min_coins
        return memo[x]
    result = helper(amount)
    return result if result != float('inf') else -1

coins = [1, 2, 5]
amount = 11
print(coin_change(coins, amount))

