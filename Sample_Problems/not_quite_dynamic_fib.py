'''
I don't think this would be considered dynamic programming because there's no recursion,
but it's my preferred solution. The time complexity should still = O(n), and I don't have 
to write any conditionals for n = 0 or n = 1. 

I haven't included any validation here. It's a toy problem. There's no need to complicate the code. 
'''

fn = [0, 1]

def fib(n):
    m = len(fn)
    # If the param is an int < len(fn), then fib(n) is already in the list. 
    if n <= m: f = fn[n]
    else: 
        while m <= n:
            f = fn[-2] + fn[-1]
            fn.append(f)
            m+=1
    return f"Fib of {n} is {f}"

print(fib(8))
