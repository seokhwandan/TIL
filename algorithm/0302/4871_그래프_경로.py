import sys
sys.stdin = open('4871.txt')

def dfs2(v):
    # 가지치기
    if v == e:
        return 1

    # 방문체크
    visited[v] = 1
    # v에 인접한 정점
    for w in range(1, V + 1):
        if adj[v][w] == 1 and visited[w] == 0:
        # 재귀호출
            if dfs2(w) == 1:
                return 1

def dfs(v):
    # 가지치기
    global flag
    if v == e:
        flag = 1
        return

    # 방문체크
    visited[v] = 1
    # v에 인접한 정점
    for w in range(1, V + 1):
        if adj[v][w] == 1 and visited[w] == 0:
        # 방문하지 않았으면 재귀 호출
            dfs(w)


T = int(input())
for tc in range(1, T + 1):
    flag = 0 # 도착하면 1로 바뀜
    # 정점, 간선
    V, E = map(int, input().split())
    # 인접행렬
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    # 방문체크
    visited = [0] * (V + 1)
    for _ in range(E):
        u, v  = map(int, input().split())
        adj[u][v] = 1 # 방향성이 있음
    s, e = map(int, input().split())

    dfs(s)
    print('#{} {}'.format(tc, flag))