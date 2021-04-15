import sys
sys.stdin = open('4012.txt')

from itertools import combinations

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    minV = 99999

    for a in combinations(range(N), N // 2):
        b = []
        for i in range(N):
            if i not in a:
                b.append(i)
    
        sumA = sumB = 0
        for i in range(N // 2 - 1):
            for j in range(i + 1, N // 2):
                sumA += arr[a[i]][a[j]] + arr[a[j]][a[i]]
                sumB += arr[b[i]][b[j]] + arr[b[j]][b[i]]

        minV = min(abs(sumA - sumB), minV)

    print('#{} {}'.format(t, minV))