import sys
sys.stdin = open('1861.txt')

from collections import deque
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def bfs(r, c):

    cnt = 1
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == arr[r][c] + 1:
                q.append((nr, nc))
                cnt += 1
    return cnt


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    start = 0
    maxV = 0
    q = deque()
    for r in range(N):
        for c in range(N):
            if bfs(r, c) > maxV:
                maxV = bfs(r, c)
                start = arr[r][c]
            if maxV == bfs(r, c):
                start = min(arr[r][c], start)

    
    print('#{} {} {}'.format(t, start, maxV))