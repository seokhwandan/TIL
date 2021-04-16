import sys
sys.stdin = open('1970.txt')

m = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
T = int(input())
for t in range(1, T + 1):
    print('#{}'.format(t))
    ans = [0] * 8
    N = int(input())
    i = 0
    cnt = 0
    while i < len(m):
        n = N // m[i] 
        if n >= 1:
            N = N - m[i] * n
            ans[i] = n
            i += 1
        else:
            i += 1
    print(*ans)