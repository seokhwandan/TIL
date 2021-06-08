import random

for i in range(50):
    num = random.sample(range(2, 10001), 1)
    a, b = -10000, 10000
    arr = random.sample(range(a, b), num)
    N = len(arr)
    M = sum(random.sample(arr, 2))
    print(N, M)
    print(arr)