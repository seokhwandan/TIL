import sys
sys.stdin = open('1953.txt')
from collections import deque

pipe = {
    0: (),
    1: [(1, 0), (0, 1), (-1, 0), (0, -1)],
    2: [(1, 0), (-1, 0)],
    3: [(0, 1), (0, -1)],
    4: [(-1, 0), (0, 1)] ,
    5: [(1, 0), (0, 1)],
    6: [(1, 0), (0, -1)],
    7: [(-1, 0), (0, -1)],
}
T = int(input())
for t in range(1, T + 1):
    h, w, hr, hc, time = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(h)]
    q = deque([(hr, hc)])
    visited = [[0] * w for _ in range(h)]
    visited[hr][hc] = 1
    cnt = 1

    while q:
        r, c = q.popleft()
        for dr, dc in pipe[tunnel[r][c]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w:
                if (-dr, -dc) in pipe[tunnel[nr][nc]]:
                    if not visited[nr][nc] and tunnel[nr][nc]:
                        visited[nr][nc] = visited[r][c] + 1
                        q += [(nr, nc)]
                        if visited[nr][nc] <= time:
                            cnt += 1
    print('#{} {}'.format(t, cnt))