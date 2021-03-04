import sys
sys.stdin = open('5102.txt')

def bfs(v):
    global d
    q.append(v) # v enQueue
    visited[v] = 1 # visited 체크
    while q: # q가 not empty
        t = q.pop(0) # deQueue
        for w in range(1, V + 1): # t에 인접한 모든 정점 w에 대해서
            if adj[t][w] == 1 and visited[w] == 0: # 방문하지 않았으면
                q.append(w) # enQueue
                visited[w] = visited[t] + 1 # 거리 증가
                if w == G: # 도착노드와 같으면
                    d = visited[G] - 1
                    
T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split()) # 노드의 갯수, 간선의 갯수
    adj = [[0] * (V + 1) for _ in range(V + 1)] # 인접행렬
    visited = [0] * (V + 1) # 방문체크
    for i in range(E):
        s, e = map(int, input().split()) # 이어진 노드
        # 양방향 노드
        adj[s][e] = 1
        adj[e][s] = 1
    S, G = map(int, input().split()) # 출발노드, 도착노드
    q = []
    d = 0 # 노드 거리
    bfs(S)
    print('#{} {}'.format(t, d))