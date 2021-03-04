import sys
sys.stdin = open('1227.txt')

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs(r, c):
    global flag
    q.append([r, c])
    while q:
        t = q.pop(0)
        sr, sc = t[0], t[1]
        for dr, dc in d:
            nr = sr + dr
            nc = sc + dc
            if 0 <= nr < 100 and 0 <= nc < 100:
                if maze[nr][nc] == 0:
                    q.append([nr, nc])
                    maze[nr][nc] = 1
                if maze[nr][nc] == 3:
                    flag = 1
                    return

for t in range(10):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(100)]
    q = []
    flag = 0
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                r, c = i, j
    bfs(r, c)
    print('#{} {}'.format(N, flag))