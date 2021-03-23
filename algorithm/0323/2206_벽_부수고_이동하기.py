import sys
sys.stdin = open('2206.txt')

from collections import deque

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def f(r, c, k):
    q.append([r, c, k])
    visited[r][c][k] = 1

    while q:
        cr, cc, ck = q.popleft()

        if cr == N - 1 and cc == M - 1:
            return visited[cr][cc][ck]

        for dr, dc in d:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 0 and visited[nr][nc][ck] == 0:
                    visited[nr][nc][ck] = visited[cr][cc][ck] + 1
                    q.append([nr, nc, ck])
                if arr[nr][nc] == 1 and ck == 1:
                    visited[nr][nc][0] = visited[cr][cc][ck] + 1
                    q.append([nr, nc, 0])
    return -1


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
q = deque()
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

ans = f(0, 0, 1)
print(ans)