def factorial(n):
    """The function compute factorial of numbers
    
    input:
        -n : the number to specify
    output:
        value: factorial of the number
    """
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

facto = factorial(4)
print(facto)