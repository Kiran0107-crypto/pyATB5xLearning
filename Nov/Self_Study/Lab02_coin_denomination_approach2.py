def min_coins_and_used(amount, coins):
    # Step 1: Initialize dp array
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins for amount 0

    # Array to track coins used to form each amount
    coin_used = [-1] * (amount + 1)

    # Step 2: Fill dp array using the coins
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    # Step 3: Retrieve the coins used
    if dp[amount] == float('inf'):
        return "Not possible to form the amount with the given denominations.", []

    # Trace back the coins used
    used_coins = []
    remaining_amount = amount
    while remaining_amount > 0:
        coin = coin_used[remaining_amount]
        used_coins.append(coin)
        remaining_amount -= coin

    return dp[amount], used_coins


# User Input
try:
    amount = int(input("Enter the amount: "))
    coins = list(map(int, input("Enter the coin denominations (comma-separated): ").split(',')))

    min_coins, coins_used = min_coins_and_used(amount, coins)

    if isinstance(min_coins, str):  # Handle case where amount cannot be formed
        print(min_coins)
    else:
        print(f"Minimum number of coins needed: {min_coins}")
        print(f"Coins used: {coins_used}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
