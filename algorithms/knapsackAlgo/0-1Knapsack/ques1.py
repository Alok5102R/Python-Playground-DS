# Example usage:

price = [5, 10, 20, 15, 12, 7, 4, 17]
article = [4, 5, 10, 18, 13, 9, 18, 7]
Budget = 25

# Buy max article at given budget.

def max_articles_within_budget(prices, articles, budget):
    n = len(prices)
    dp = [0] * (budget + 1)
    selected_indices = [[] for _ in range(budget + 1)]
    for i in range(n):
        for j in range(budget, prices[i] - 1, -1):
            if dp[j] < dp[j - prices[i]] + articles[i]:
                print(str(dp[j]) + " " + str(dp[j - prices[i]] + articles[i]))
                dp[j] = dp[j - prices[i]] + articles[i]
                selected_indices[j] = selected_indices[j - prices[i]] + [i]

    return dp[budget], selected_indices[budget]


max_articles, indices = max_articles_within_budget(price, article, Budget)
print(f"Maximum articles you can buy within a budget of ${Budget}: {max_articles}")
print(f"Indices of selected prices: {indices}")

