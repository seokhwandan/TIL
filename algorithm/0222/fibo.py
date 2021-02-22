def fibo1(n):
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n - 1) + fibo1(n - 2))
    return memo[n]

memo = [0, 1]
print(fibo1(40))

memo2 = [-1] * 21
memo2[0] = 0
memo2[1] = 1
def fibo2(n):
    if memo2[n] == -1:
        memo2[n] = fibo2(n - 1) + fibo2(n - 2)
    return memo2[n]
print(fibo2(10))