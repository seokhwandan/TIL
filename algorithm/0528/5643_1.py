import sys
sys.stdin = open('5643.txt')

def inDFS(v):
    checked[v] = 1
    for w in range(1, m + 1):
        if adj[v][w] == 1 and checked[w] == 0:
            inDFS(w)
    
def outDFS(v):
    checked[v] = 1
    print(v, end=' ')
    for w in range(1, m + 1):
        if adj[w][v] == 1 and checked[w] == 0:
            outDFS(w)

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
        adj[b][a] = 1
    
    print(outDFS(1))
    # cnt = 0
    # for i in range(1, m + 1):
    #     for j in range(1, m + 1):
    #         checked[i] = 1
    #         if adj[i][j] == 1 and checked[j] == 0:
    #             checked[j] = 1
    #     print(checked)