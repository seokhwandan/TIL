import sys
sys.stdin = open('5250.txt')

from collections import deque

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def dijkstra(arr):
    distance[0][0] = 0
    q.append((0, 0))

    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                fuel = 1
                if arr[nr][nc] > arr[r][c]:
                    fuel += arr[nr][nc] - arr[r][c]
                
                if distance[nr][nc] > distance[r][c] + fuel:
                    distance[nr][nc] = distance[r][c] + fuel
                    q.append((nr, nc))

T = int(input())
for t in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = float('inf')
    distance = [[minV] * N for _ in range(N)]
    q = deque()
    dijkstra(arr)

    print('#{} {}'.format(t, distance[N -1][N - 1]))
