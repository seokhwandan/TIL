import sys
sys.stdin = open('1249.txt')

from collections import deque

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def bfs(arr):
    time[0][0] = 0
    q.append((0, 0))

    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                recovery = arr[nr][nc]
                
                if time[nr][nc] > time[r][c] + recovery:
                    time[nr][nc] = time[r][c] + recovery
                    q.append((nr, nc))

T = int(input())
for t in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    minV = float('inf')
    time = [[minV] * N for _ in range(N)]
    q = deque()
    bfs(arr)

    print('#{} {}'.format(t, time[N -1][N - 1]))