import sys
sys.stdin = open('1219.txt')

def DFS(v):
    visited[v] = 1

    for w in range(1, 101):
        if adj[v][w] == 1 and visited[w] == 0:
            DFS(w)

for t in range(10):
    tc, E = map(int, input().split())
    tmp = list(map(int, input().split()))
    adj = [[0] * 101 for _ in range(101)]
    visited = [0] * 101
    for i in range(E):
        start, end = tmp[2 * i], tmp[(2 * i) + 1]
        adj[start][end] = 1
    DFS(0)
    res = 1
    if not visited[99]:
        res = 0
    
    print('#{} {}'.format(tc, res))