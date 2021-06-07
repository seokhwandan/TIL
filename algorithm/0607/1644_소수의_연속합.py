def is_prime(n):
    table = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if table[i]:
            for j in range(i * 2, n + 1, i):
                table[j] = False
    
    return [i for i in range(2, n + 1) if table[i]]

def solve():
    primes = is_prime(N)
    if not primes:
        return 0
    
    ans = 0
    start, end = 0, 0
    first = primes[0]
    while start <= end:
        if first < N:
            end += 1
            if end < len(primes):
                first += primes[end]
            else:
                break
        else:
            if first == N:
                ans += 1
            first -= primes[start]
            start += 1
    return ans

N = int(input())
print(solve())