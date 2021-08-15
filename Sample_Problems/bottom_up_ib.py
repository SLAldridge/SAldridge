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
print(fib(0))
print(fib(1))
print(fib(2))

# Alternatively, save only the numbers used for calculating the next in the series. 
# This reduces space complexity, but will increase total time complexity if the function is called more than once. 
def fib2(n):
    fn2 = [0, 1]
    if n in [0, 1]: f = n
    else: 
        i = len(fn2)
        while i <= n:
            f = fn2[-2] + fn2[-1]
            fn2.pop(0)
            fn2.append(f)
            i+=1
    print(fn2)
    return f"Fib of {n} is {f}"

print(fib2(8))
print(fib2(32))
print(fib2(2))
print(fib2(0))
print(fib2(32))
