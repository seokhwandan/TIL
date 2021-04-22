'''
7 11
0 5 60
0 1 32
0 2 31
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
def prim():
    # 시작점 0으로 세팅
    total = 0
    u = 0     # 시작점을 0으로 설정
    D[u] = 0

    # 정점을 V개 선택
    for i in range(V):
        # 가중치가 최소인 정점을 찾기
        min = 987654321
        for v in range(V):
            if visited[v] == 0 and min > D[v]:
                min = D[v]
                u = v
        # 방문처리
        visited[u] = 1
        total += adj[PI[u]][u]

        # 인접한 정점들의 가중치 업데이트
        for v in range(V):
            if adj[u][v] != 0 and visited[v] == 0 and adj[u][v] < D[v]:
                D[v] = adj[u][v]
                PI[v] = u
    return total

V, E = map(int, input().split())
adj = [[0] * V for _ in range(V)]
#  초기화 작업
D = [987654321] * V     # 가중치를 모두 무한대
PI = list(range(V))           # 내부모는 나다.
visited = [0] * V       # 방문체크

#입력
for i in range(E):
    edge = list(map(int, input().split()))
    adj[edge[0]][edge[1]] = edge[2]     #방향성없음
    adj[edge[1]][edge[0]] = edge[2]  # 방향성있음

print(prim())   # MST의 간선 합
