import sys
sys.stdin = open('11763.txt')

def dfs(office):
    global sumV, ans

    if sumV < ans:
        visited[office] = 1

        if sum(visited) == N:
            sumV += arr[office][0]
            if sumV < ans:
                ans = sumV
            sumV -= arr[office][0]
        
        for i in range(N):
            if not visited[i]:
                sumV += arr[office][i]
                dfs(i)
                sumV -= arr[office][i]

        visited[office] = 0
    
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans, sumV = 1000, 0
    dfs(0)
    print('#{} {}'.format(t, ans))