import sys
sys.stdin = open('1795.txt')

import heapq

def dijkstra(arr, s):
    distance = [INF] * (N + 1)
    distance[s] = 0
    heapq.heappush(q, (0, s))

    while q:
        d, v = heapq.heappop(q)

        for i in range(1, N + 1):
            if arr[v][i] and arr[v][i] + distance[v] < distance[i]:
                distance[i] = arr[v][i] + distance[v]
                heapq.heappush(q, (distance[i], i))

    return distance[:]

T = int(input())
for t in range(1, T + 1):
    N, M, X = map(int, input().split())
    go = [[0] * (N + 1) for _ in range(N + 1)]
    back = [[0] * (N + 1) for _ in range(N + 1)] 
    INF = float('inf')
    q = []
    for i in range(M):
        x, y, c = map(int, input().split())
        go[x][y] = c
        back[y][x] = c
    
    go_X = dijkstra(go, X)
    back_X = dijkstra(back, X)

    ans = 0
    for i in range(1, N + 1):
        ans = max(ans, go_X[i] + back_X[i])

    print('#{} {}'.format(t, ans))