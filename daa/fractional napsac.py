# Fractional Knapsack Problem using Greedy Method

def fractional_knapsack(value, weight, capacity):
    n = len(value)
    # Calculate value/weight ratio
    ratio = [(value[i] / weight[i], value[i], weight[i]) for i in range(n)]
    
    # Sort items by ratio in descending order
    ratio.sort(reverse=True)

    total_value = 0.0  # total profit
    for r, v, w in ratio:
        if capacity >= w:
            # Take the whole item
            total_value += v
            capacity -= w
        else:
            # Take fractional part of the item
            total_value += r * capacity
            break

    return total_value


n = int(input("Enter number of items: "))
value = []
weight = []

for i in range(n):
    v = float(input(f"Enter value of item {i+1}: "))
    w = float(input(f"Enter weight of item {i+1}: "))
    value.append(v)
    weight.append(w)

capacity = float(input("Enter capacity of knapsack: "))

max_value = fractional_knapsack(value, weight, capacity)
print(f"\nMaximum value in Knapsack = {max_value:.2f}")

# | Type                 | Explanation                                      | Complexity     |
# | -------------------- | ------------------------------------------------ | -------------- |
# | **Time Complexity**  | Sorting `n` items → O(n log n); selection → O(n) | **O(n log n)** |
# | **Space Complexity** | Storing ratios, weights, values                  | **O(n)**       |


# | Question                                 | Answer                                                                                                         |
# | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
# | What is the Greedy method?               | It builds up a solution piece by piece, always choosing the next piece that offers the most immediate benefit. |
# | Why is this problem called “fractional”? | Because we are allowed to take fractional parts of an item.                                                    |
# | What is the time complexity?             | O(n log n) due to sorting.                                                                                     |
# | Can we solve 0/1 Knapsack using greedy?  | No, because the greedy approach doesn’t guarantee the optimal solution for 0/1 Knapsack.                       |
# | What is the key formula used?            | ratio = value / weight                                                                                         |
# | Why do we sort by ratio?                 | To maximize value per unit weight.                                                                             |
