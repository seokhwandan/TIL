'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
# 7 = 정점의 갯수, 8 = 간선의 갯수

V, E = map(int, input().split())
tmp = list(map(int, input().split()))
adj = [[0] * (V + 1) for _ in range(V + 1)] # 인접행렬

for i in range(E):
    s, e = tmp[2 * i], tmp[2 * i + 1]
    adj[s][e] = 1
    adj[e][s] = 1

for i in range(V + 1):
    print('{} {}'.format(i, adj[i]))