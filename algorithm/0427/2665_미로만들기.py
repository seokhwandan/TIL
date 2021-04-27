import sys
sys.stdin = open('2665.txt')

from collections import deque

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def bfs(r, c, cnt):
    q.append((r, c, cnt))

    while q:
        r, c, cnt = q.popleft()

        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] == 1:
                    if visited[nr][nc] > cnt:
                        visited[nr][nc] = cnt
                        q.append((nr, nc, cnt))
                elif arr[nr][nc] == 0:
                    if visited[nr][nc] > cnt + 1:
                        visited[nr][nc] = cnt + 1
                        q.append((nr, nc, cnt + 1))

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[float('inf')] * n for _ in range(n)]
q = deque()
bfs(0, 0, 0)
print(visited[n - 1][n - 1])
