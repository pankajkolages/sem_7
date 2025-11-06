# Recursive Fibonacci Program

def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


n = int(input("Enter the number of terms: "))
print("Fibonacci Series (Recursive):")
for i in range(n):
    print(fib_recursive(i), end=" ")

# Non-Recursive (Iterative) Fibonacci Program

def fib_iterative(n):
    a, b = 0, 1
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    series = [0, 1]
    for i in range(2, n):
        c = a + b
        series.append(c)
        a, b = b, c
    return series


n = int(input("\nEnter the number of terms: "))
print("Fibonacci Series (Non-Recursive):")
print(fib_iterative(n))


#  Time Complexity

# One loop runs n times → O(n) time.

# Space Complexity

# If only printing → O(1)

# If storing series → O(n) (for array storage).


# | Question                                             | Answer                                                                                     |
# | ---------------------------------------------------- | ------------------------------------------------------------------------------------------ |
# | What is the Fibonacci series?                        | A sequence where each number is the sum of the previous two numbers. (0, 1, 1, 2, 3, 5, …) |
# | Difference between recursive and iterative approach? | Recursive calls itself; iterative uses loops. Iterative is faster and uses less memory.    |
# | Time complexity of recursive Fibonacci?              | O(2ⁿ) — exponential.                                                                       |
# | Time complexity of iterative Fibonacci?              | O(n).                                                                                      |
# | Space complexity of recursive Fibonacci?             | O(n) due to recursion stack.                                                               |
# | Space complexity of iterative Fibonacci?             | O(1) if not storing the series, O(n) if stored.                                            |
