

def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    # Reconstruct LCS
    lcs_str = []
    while m > 0 and n > 0:
        if X[m - 1] == Y[n - 1]:
            lcs_str.append(X[m - 1])
            m -= 1
            n -= 1
        elif dp[m - 1][n] > dp[m][n - 1]:
            m -= 1
        else:
            n -= 1

    return ''.join(reversed(lcs_str))

# Example usage:
X = "AGGTAB"
Y = "GXTXAYB"
print("LCS:", lcs(X, Y))  # Output: "GTAB"