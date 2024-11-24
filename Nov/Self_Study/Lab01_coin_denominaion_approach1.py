
def min_coins(coins, target_amount):
    # revering the list of coins denomination
    coins.sort(reverse=True)
    print("Reverse of list of Coins denomination",coins)
    # Dividing the target amount by the largest coin denomination, it is done to optimize the algo
    no_of_max_coins= target_amount//coins[0]
    target_amount=target_amount%coins[0]
    print("No of Max Coins after dividing amount by max coin denomination:\n",no_of_max_coins)
    #Initializing dp table to infinity for all amounts
    dp = [float('inf')] * (target_amount + 1)
    print("Dp after initializing to infinity to all elements:\n",dp)
    #Base Case, as for amount 0, 0 coins will be required
    dp[0] = 0
    print("Print dp[0]:\n",dp[0])
    #Filling the dp table
    for amount in range(1, target_amount + 1):
        print("First Loop:\n",amount)
        for coin in coins: #first loop is to run for all coin denomination 1 by one
            print("2nd Loop",coin)
            if coin<=amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
                print("DP amount:\n", dp[amount])
                print("Printing DP inside loops:\n",dp)
    dp[target_amount]=dp[target_amount] +no_of_max_coins
    print(dp[target_amount])
    return dp[target_amount] if dp[target_amount] != float('inf') else -1


coins = [2,5,10,20,50,100]
target_amount = 203
result = min_coins(coins, target_amount)
print("No of minimum coins:\n",result)
