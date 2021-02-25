import sys
sys.stdin = open('5789.txt')

T = int(input())
for t in range(1, T + 1):
    print('#{}'.format(t), end=' ')
    N, Q = map(int, input().split())
    LR = [list(map(int, input().split()))for _ in range(Q)]
    ans = [0 for _ in range(N + 1)]
    for i in range(Q):
        for j in range(LR[i][0], LR[i][1] + 1):
            ans[j] = i + 1
    ans.pop(0)
    print(*ans)