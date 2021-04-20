import sys
sys.stdin = open('5208.txt')

def solve(arr):
    N, batteries = arr[0], arr[1:]
    destination = N - 1
    cnt = -1
    while destination:
        for i in range(destination):
            if i + batteries[i] >= destination:
                destination = i
                cnt += 1
                break
    return cnt

T = int(input())
for t in range(1, T + 1):
    arr = list(map(int, input().split()))
    print('#{} {}'.format(t, solve(arr)))