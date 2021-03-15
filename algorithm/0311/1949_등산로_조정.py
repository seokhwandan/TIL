import sys
sys.stdin = open('1949.txt')

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def find(arr):
    global max_h
    for i in range(N):
        for j in range(N):
            max_h = max(max_h, arr[i][j])

def dfs(r, c, k, move):
    global ans
    ans = max(ans, move)
    visited[r][c] = 1
    for dr, dc in d:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < N:
            if not visited[nr][nc]:
                if H[nr][nc] < H[r][c]:
                    visited[r][c] = 1
                    dfs(nr, nc, k, move + 1)
                else:
                    if H[nr][nc] - k < H[r][c]:
                        h = H[nr][nc]
                        H[nr][nc] = H[r][c] - 1
                        dfs(nr, nc, 0, move + 1)
                        H[nr][nc] = h
    visited[r][c] = 0

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    H = [list(map(int, input().split())) for _ in range(N)]
    max_h = 0
    ans = 0
    visited = [[0] * N for _ in range(N)]
    find(H)
    
    for i in range(N):
        for j in range(N):
            if H[i][j] == max_h:
                dfs(i, j, K, 1)
    print('#{} {}'.format(t, ans))
