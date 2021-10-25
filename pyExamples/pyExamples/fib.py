# Fibonacci numbers module

__all__ = ['fib']

def fib(n):
    """
    write Fibanacci series up to n
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
    
def fib2(n):
    """
    return Fibonacci serires up to n
    """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


# run only when run directly
if __name__ == '__main__':
    import sys
    fib(int(sys.argv[1]))

# give custom name other than its filename
__name__ = 'fibo'