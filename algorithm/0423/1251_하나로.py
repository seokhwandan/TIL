import sys
sys.stdin = open('1251.txt')

def check(arr):
    global ans

    cost[0] = 0
    cnt = 0

    while cnt < N:
        minC = float('inf')
        n = -1
        for i in range(N):
            if not visited[i] and cost[i] < minC:
                minC = cost[i]
                n = i

        visited[n] = 1
        ans += minC
        cnt += 1

        for i in range(N):
            if not visited[i] and cost[i] > arr[n][i]:
                cost[i] = arr[n][i]
                node[i] = n

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(i + 1, N):
            arr[i][j] = arr[j][i] = ((X[i] - X[j])**2 + (Y[i] - Y[j])**2) * E
            
    visited = [0] * N        
    cost = [float('inf')] * N
    node = [0] * N
    ans = 0

    check(arr)
    print('#{} {}'.format(t, round(ans)))

