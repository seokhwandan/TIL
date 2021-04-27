import sys
sys.stdin = open('2211.txt')

import heapq

def dijkstra(s):
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        d, s = heapq.heappop(q)

        for ce, cd in G[s]:
            if distance[ce] > distance[s] + cd:
                distance[ce] = distance[s] + cd
                visited[ce] = s
                heapq.heappush(q, (distance[ce], ce))

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for i in range(M):
    s, e, d = map(int, input().split())
    G[s].append((e, d))
    G[e].append((s, d))

distance = [float('inf')] * (N + 1)
visited = [0] * (N + 1)
q = []
dijkstra(1)

cnt = 0
for i in range(N + 1):
    if visited[i]:
        cnt += 1
for i in range(N + 1):
    if visited[i]:
        print(i, visited[i])
