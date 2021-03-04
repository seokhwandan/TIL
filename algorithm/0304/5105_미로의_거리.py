import sys
sys.stdin = open('5105.txt')

d = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 4방향 노드

def bfs(r, c):
    global distance
    visited[r][c] = 1 # visited 체크
    q.append([r, c]) # [r, c] enQueue
    while q: # q is not empty
        t = q.pop(0) # deQueue
        sr, sc = t[0], t[1]
        for dr, dc in d: # 4방향 탐색
            nr = sr + dr
            nc = sc + dc
            if 0 <= nr < N and 0 <= nc < N: # 미로 범위 내에서
                if maze[nr][nc] == 0 and visited[nr][nc] == 0: # 인접노드가 통로이고, 방문하지 않았을 경우
                    q.append([nr, nc]) # enQueue
                    visited[nr][nc] = visited[sr][sc] + 1 # 거리 증가
                if maze[nr][nc] == 3: # 도착노드에 도착했을 경우
                    distance = visited[sr][sc] - 1

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)] # 방문체크
    q = []
    distance = 0 # 미로의 거리
    # 출발위치 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2: 
                r = i
                c = j    
    bfs(r, c)
    print('#{} {}'.format(t, distance))