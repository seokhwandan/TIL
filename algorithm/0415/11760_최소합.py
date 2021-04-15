import sys
sys.stdin = open('11760.txt')

d = [(0, 1), (1, 0)]

def dfs(r, c, sumV):
    global ans

    if sumV > ans:
        return
    
    if r == N - 1 and c == N - 1:
        ans = sumV
        return
    
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:
            dfs(nr, nc, sumV + arr[nr][nc])

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 10 * 2 * N
    dfs(0, 0, arr[0][0])
    print('#{} {}'.format(t, ans))
