def knapsack(W, wt, val, n):
    # Create a 2D array to store the maximum value that can be obtained
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build the dp array from the bottom up
    for i in range(1, n + 1):
        for w in range(W + 1):
            if wt[i-1] <= w:
                # Maximum value obtained by including the current item or excluding it
                dp[i][w] = max(dp[i-1][w], val[i-1] + dp[i-1][w-wt[i-1]])
            else:
                # If the current item's weight is more than the current capacity, exclude it
                dp[i][w] = dp[i-1][w]

    # The maximum value that can be obtained with n items and capacity W
    return dp[n][W]

# Example usage
val = [60, 100, 120]  # Values of the items
wt = [10, 20, 30]     # Weights of the items
W = 50                # Maximum weight capacity of the knapsack
n = len(val)          # Number of items

print("Maximum value in Knapsack =", knapsack(W, wt, val, n))