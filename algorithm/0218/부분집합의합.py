import sys
sys.stdin = open('부분집합의합.txt')

T = int(input())
arr = list(range(1,13))
n = len(arr)
for t in range(1, T + 1):
    N, K = map(int, input().split())
    ans = 0

    for i in range(1, 1 << n):
        sum = 0
        cnt = 0
        for j in range(n):
            if i & (1 << j):
                sum += arr[j]
                cnt += 1
        if sum == K and cnt == N:
            ans += 1
    print('#{} {}'.format(t, ans))
