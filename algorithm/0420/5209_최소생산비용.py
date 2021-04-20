import sys
sys.stdin = open('5209.txt')

def dfs(i, sumV):
    global ans

    if ans < sumV:
        return

    if i == N:
        ans = min(ans, sumV)
        return
    
    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            dfs(i + 1, sumV + V[i][j])
            visited[j] = 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 9999

    dfs(0, 0)
    print('#{} {}'.format(t, ans))