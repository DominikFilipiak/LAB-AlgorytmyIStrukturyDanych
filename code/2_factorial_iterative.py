def iterative_factorial(n):        
    x = 1
    li = list(range(2, n+1))
    for each in li:
        x = x*each
        yield x
