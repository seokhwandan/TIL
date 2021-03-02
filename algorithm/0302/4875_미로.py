import sys
sys.stdin = open('4875.txt')

def dfs(r, c):
    global res
    if maze[r][c] == 3:
        res = 1
        return

    # 방문체크
    visited[r][c] = 1
    # 방향탐색
    for dr, dc in d:
        nr = r + dr
        nc = c + dc
        # N x N 범위 내에서
        if 0 <= nr < N and 0 <= nc < N:
            # 방향탐색 결과 0 이거나 3일 때
            if maze[nr][nc] == 0 or maze[nr][nc] == 3:
                # 방문하지 않은 곳이라면
                if not visited[nr][nc]:
                    # 재귀
                    dfs(nr, nc)

d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    res = 0
    # 출발점 좌표 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                r = i
                c = j
    dfs(r, c)
    print('#{} {}'.format(t, res))



