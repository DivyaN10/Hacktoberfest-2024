def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = 10  # Change this value to compute a different Fibonacci number
print(f"Fibonacci({n}) = {fibonacci_recursive(n)}")

