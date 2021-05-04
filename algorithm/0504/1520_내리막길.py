import sys
sys.stdin = open('1520.txt')

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

cnt = 0
def dfs(r, c):
    global cnt

    if r == M - 1 and c == N - 1:
        cnt += 1
        return

    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if 0 <= nr < M and 0 <= nc < N:
            if arr[nr][nc] < arr[r][c]:
                dfs(nr, nc)

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
cnt = 0
dfs(0, 0)
print(cnt)


# memoization
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

cnt = 0
def dfs(r, c):

    if r == M - 1 and c == N - 1:
        return 1

    if dp[r][c] == -1:
        dp[r][c] = 0

        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < M and 0 <= nc < N:
                if arr[nr][nc] < arr[r][c]:
                    dp[r][c] += dfs(nr, nc)

    return dp[r][c]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
print(dfs(0, 0))
