for i in range(1, 100):
    if i%5 == 0: 
        print("Pop" if i%3 else "Buzz")
    elif i%3 == 0: print("Fizz")
    else: print(i)
        