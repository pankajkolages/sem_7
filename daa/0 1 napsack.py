# 0-1 Knapsack Problem using Dynamic Programming

def knapsack_01(values, weights, capacity):
    n = len(values)
    # Create a DP table of size (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Include item i-1 or exclude it
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # Cannot include item i-1
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]  # The last cell contains the answer


# Driver Code
n = int(input("Enter number of items: "))
values = []
weights = []

for i in range(n):
    values.append(int(input(f"Enter value of item {i + 1}: ")))
    weights.append(int(input(f"Enter weight of item {i + 1}: ")))

capacity = int(input("Enter capacity of knapsack: "))

max_value = knapsack_01(values, weights, capacity)
print(f"\nMaximum value in 0/1 Knapsack = {max_value}")


# | Type                 | Explanation              | Complexity   |
# | -------------------- | ------------------------ | ------------ |
# | **Time Complexity**  | Two nested loops (n × W) | **O(n × W)** |
# | **Space Complexity** | DP table of size (n × W) | **O(n × W)** |


# | Question                                                    | Answer                                                                                                |
# | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
# | What is the 0/1 Knapsack problem?                           | A problem where each item can be either taken completely (1) or not taken (0).                        |
# | Can we take fractional items?                               | No, only full items are allowed.                                                                      |
# | Which approach gives optimal solution?                      | Dynamic Programming or Branch and Bound.                                                              |
# | Time Complexity of DP solution?                             | O(n × W)                                                                                              |
# | Why greedy doesn’t work here?                               | Because taking highest value/weight ratio doesn’t guarantee optimality when fractions aren’t allowed. |
# | What is the difference between Fractional and 0/1 Knapsack? | Fractional allows splitting items; 0/1 does not.                                                      |
# | What is stored in DP[i][w]?                                 | The maximum profit for first i items and capacity w.                                                  |
