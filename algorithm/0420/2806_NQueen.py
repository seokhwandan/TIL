import sys
sys.stdin = open('2806.txt')

d = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

def check(r, c):
    if row[r] == 1:
        return 0

    if col[c] == 1:
        return 0
    
    for dr, dc in d:
        for i in range(N):
            nr, nc = r + dr * i, c + dc * i
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc]:
                return 0
    return 1

def dfs(r):
    global ans

    if r == N:
        ans += 1
        return
    
    for c in range(N):
        if check(r, c):
            row[r] = col[c] = 1
            visited[r][c] = 1
            dfs(r + 1)
            row[r] = col[c] = 0
            visited[r][c] = 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())

    row = [0] * N
    col = [0] * N
    visited = [[0] * N for _ in range(N)]
    ans = 0
    dfs(0)
    print('#{} {}'.format(t, ans))
