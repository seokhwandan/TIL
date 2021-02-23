import sys
sys.stdin = open('4871.txt')

def DFS(s): # 시작 정점
    # visited check
    visited[s] = 1
    # print(s, end=' ')

    for w in range(1, V + 1):
        if adj[s][w] == 1 and visited[w] == 0:
            DFS(w)

T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)] # 인접행렬 초기화
    visited = [0] * (V + 1)
    for i in range(E):
        start, end = node[i][0], node[i][1]
        adj[start][end] = 1
    DFS(S)
    res = 1
    if not visited[G]:
        res = 0
    print('#{} {}'.format(t, res))