import time

# Brute-force approach to compute the nth Fibonacci number => O(2^n) time complexity
def fibonacci_brute_force(n):
    """The function compute the nth Fibonacci number using brute-force approach
    
    input:
        -n : the number to specify
    output:
        value: the nth Fibonacci number
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_brute_force(n-1) + fibonacci_brute_force(n-2)


def fibonacci(n, memo={}):
    """The function compute the nth Fibonacci number
    
    input:
        -n : the number to specify
        -memo : a dictionary to store previously computed values
    output:
        value: the nth Fibonacci number
    """
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]


if __name__ == "__main__":
    # Test brute-force with smaller number (since it's slow)
    start_time = time.time()
    result_bf = fibonacci_brute_force(30)
    end_time = time.time()
    print(f"Brute-force fib(30): {result_bf}")
    print(f"Execution time: {end_time - start_time:.6f} seconds\n")
    
    # Test memoized version with larger number
    start_time = time.time()
    result = fibonacci(50)
    end_time = time.time()
    print(f"Memoized fib(50): {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")