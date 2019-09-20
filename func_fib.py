def func_fib(n):
    def go(i, x, y):
        if i < 2:
            return y
        else:
            return go(i - 1, y, x + y)
    return go(n, 0, 1)


if __name__ == "__main__":
    print(func_fib(10))