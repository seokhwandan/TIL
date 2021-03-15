import sys
sys.stdin = open('4012.txt')

from itertools import combinations

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    taste = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    minV = 9999
    cA = list(combinations(range(N), N // 2))
    for a in cA:
        visited = [0 for _ in range(N)]
        for i in a:
            visited[i] = 1
        b = []
        for i in range(N):
            if not visited[i]:
                b.append(i)
        sumA = 0
        sumB = 0
        for i in range(N // 2 - 1):
            for j in range(i + 1, N // 2):
                sumA += taste[a[i]][a[j]] + taste[a[j]][a[i]]
                sumB += taste[b[i]][b[j]] + taste[b[j]][b[i]]
        
        res = abs(sumA - sumB)
        if res < minV:
            minV = res
    print('#{} {}'.format(t, minV))