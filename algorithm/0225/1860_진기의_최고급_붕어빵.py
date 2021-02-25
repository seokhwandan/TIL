import sys
sys.stdin = open('1860.txt')

T = int(input())
for t in range(1, T + 1):
    res = 'Possible'
    N, M, K = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    for i in range(N):
        if (p[i] // M) * K < i + 1:
            res = 'Impossible'
    print('#{} {}'.format(t, res))