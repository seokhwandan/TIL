import sys
sys.stdin = open('5251.txt')

import heapq

def dijkstra(arr):
    heapq.heappush(q, (0, 0))

    while q:
        e, d = heapq.heappop(q)
        if not visited[s]:
            visited[e] = 1
            
            for n1, n2 in node[e]:
                if distance[n1] > d + n2:
                    distance[n1] = d + n2
                    heapq.heappush(q, (n1, distance[n1]))

T = int(input())
for t in range(1, 1 + T):
    N, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    minV = float('inf')
    distance = [minV] * (N + 1)
    node = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    q = []

    for s, e, d in arr:
        node[s].append((e, d))

    dijkstra(arr)
    print('#{} {}'.format(t, distance[N]))
