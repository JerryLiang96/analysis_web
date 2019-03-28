def xxx():
    for i in range(10):
        yield i


x = xxx()
try:
    while True:
        s = next(x)
        print(s)
except StopIteration:
    print(1111)
except Exception:
    print(2222)
