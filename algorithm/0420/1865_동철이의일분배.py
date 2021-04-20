import sys
sys.stdin = open('1865.txt')

def dfs(i, probability):
    global maxV

    if maxV >= probability: # 1 이하의 수는 곱할수록 작아지므로
        return

    if i == N:
        maxV = max(maxV, probability)
        return
    
    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            dfs(i + 1, probability * P[i][j] / 100)
            visited[j] = 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    maxV = 0
    dfs(0, 1)
    print('#{} {:.6f}'.format(t, maxV * 100))