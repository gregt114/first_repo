
def fibonacci(n: int) -> int:
    """
    Recursive implementation to calculate the n-th Fibonacci number
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(32):
    print(f"{i} : {fibonacci(i)}")
