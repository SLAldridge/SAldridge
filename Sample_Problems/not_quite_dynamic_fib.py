'''
I don't think this would be considered dynamic programming because there's no recursion,
but the time complexity should still = O(n), and I don't have to write any conditionals
for n = 0 or n = 1
If I were defining fn outside of the function, I'd probably use a dictionary instead
because this function relies on the list being ordered.
'''

def fib(n):
    fn = [0, 1]
    m = len(fn)
    while m <= n:
        f = fn[-2] + fn[-1]
        fn.append(f)
        m+=1
    return f"Fib of {n} is {f}"

print(fib(8))
