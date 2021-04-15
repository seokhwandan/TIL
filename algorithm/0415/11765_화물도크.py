import sys
sys.stdin = open('11765.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: x[1])
    end = arr[0][1]
    ans = 1
    i = 1
    while i < N:
        if arr[i][0] >= end:
            end = arr[i][1]
            ans += 1
        i += 1
    print('#{} {}'.format(t, ans))