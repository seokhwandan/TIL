'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def BFS(v):
    # v 를 enQ(visited 체크)
    Q.append(v)
    visited[v] = 1
    print(v, end= ' ')
    # Q 가 not empty:
    while Q:
        # t <- deQ, 부모
        t = Q.pop(0)
        # t 에 인접한 모든 정점 w에 대해서, w : 자식
        for w in range(1, V + 1):
            # w가 not visited 이면
            if adj[t][w] == 1 and visited[w] == 0:
                # enQ
                Q.append(w)
                # visited[w] = 1
                visited[w] = visited[t] + 1
                print(w, end= ' ')

V, E = map(int, input().split()) # 정점, 간선
temp = list(map(int, input().split()))
adj = [[0] * (V + 1) for _ in range(V + 1)] # 인접행렬
Q = []
visited = [0] * (V + 1)
# 인접행렬 입력
for i in range(E):
    s, e = temp[2 * i], temp[2 * i + 1] # 한쌍 씩 가져오기
    # 무향 그래프
    adj[s][e] = 1
    adj[e][s] = 1

BFS(1)
print(visited)