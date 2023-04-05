
import math

phi = (1 + math.sqrt(5)) / 2


def fibonacci(n: int) -> int:
    """
    Compute n-th Fibonacci number using formula
    """
    result = (phi**n - (-phi)**(-n)) / math.sqrt(5)
    return round(result)

for i in range(0, 32):
    print(f"{i} : {fibonacci(i)}")
