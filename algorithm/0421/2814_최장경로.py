import sys
sys.stdin = open('2814.txt')

def dfs(n, cnt):
    global maxD

    visited[n] = 1
    maxD = max(maxD, cnt)

    for i in G[n]:
        if not visited[i]:
            dfs(i, cnt + 1)

    visited[n] = 0

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    G = [[] for _ in range(N + 1)]
    for s, e in arr:
        G[s].append(e)
        G[e].append(s)

    visited = [0] * (N + 1)
    maxD = 0
    for i in range(N):
        dfs(i, 1)
    print('#{} {}'.format(t, maxD))
