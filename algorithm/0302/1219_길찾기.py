import sys
sys.stdin = open('1219.txt')

def dfs(v):
    # 가지치기
    global flag
    if v == GOAL:
        flag = 1
        return

    visited[v] = 1
    for w in range(SIZE):
        if adj[v][w] and not visited[w]:
            dfs(w)

T = 10
SIZE = 100
S = 0
GOAL = 99
for tc in range(1, T + 1):
    flag = 0
    no, E = map(int, input().split())
    temp = list(map(int, input().split())) # 간선들의 정보
    # 인접행렬
    adj = [[0] * SIZE for _ in range(SIZE)]
    # 방문체크
    visited = [0] * SIZE
    # 입력받기
    for i in range(0, len(temp), 2):
        adj[temp[i]][temp[i + 1]] = 1 # 방향성이 있음
    dfs(S)
    print('#{} {}'.format(tc, flag))