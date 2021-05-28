import sys
sys.stdin = open('5643.txt')

big = []
def DFS(v):
    checked[v] = 1
    big.append(v)
    for w in range(1, m + 1):
        if adj[v][w] == 1 and checked[w] == 0:
            DFS(w)
    return big

small = []
def rDFS(v):
    checked[v] = 1
    small.append(v)
    for w in range(1, m + 1):
        if adj[w][v] == 1 and checked[w] == 0:
            rDFS(w)
    return small

T = int(input())
for t in range(1, T + 1):
    n = int(input()) # 학생들의 수
    m = int(input()) # 키를 비교한 횟수
    tmp = [list(map(int, input().split())) for _ in range(m)]
    checked = [0] * (m + 1)
    adj = [[0] * (m + 1) for _ in range(m + 1)]
    for i in range(m):
        a, b = tmp[i][0], tmp[i][1]
        adj[a][b] = 1

    # i = 1
    # cnt = 0
    # while i < m + 1:
    #     ans = DFS(i) + rDFS(i)
    #     if len(set(ans)) == 6:
    #         cnt += 1
    #         break
    #     else:
    #         i += 1
    # print('#{} {}'.format(t, cnt))