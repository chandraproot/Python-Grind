


def fibonacci(n, pre_map=None):
    if pre_map is None:
        pre_map = {}
    if n in pre_map:
        # print(pre_map)
        return pre_map[n]
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib = fibonacci(n-1, pre_map) + fibonacci(n-2, pre_map)
        pre_map[n] = fib
        return fib


f = [fibonacci(i) for i in range(2,20)]
print(f)
