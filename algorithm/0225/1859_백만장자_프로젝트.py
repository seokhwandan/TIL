import sys
sys.stdin = open('1859.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    tmp = list(map(int, input().split()))[::-1]
    ans = 0
    max_value = tmp[0]
    for i in range(1, N):
        if max_value > tmp[i]:
            ans += max_value - tmp[i]
        else:
            max_value = tmp[i]
    print('#{} {}'.format(t, ans))
