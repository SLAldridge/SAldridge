fn = [0, 1]

def fib(n):
    m = len(fn)
    if n < m:
        f = fn[n]
    else: 
        for int in range(m, n):
            f = fn[-2] + fn[-1]
            fn.append(f)
    return f"Fib of {n} is {f}"

print(fib(8))
