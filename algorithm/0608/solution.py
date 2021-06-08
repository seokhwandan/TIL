import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
start, end = 0, N - 1
minV = float('inf')
ans = []

while start < end:
    sumV = arr[start] + arr[end]

    if abs(sumV - M) == minV and [arr[start], arr[end]] not in ans:
        ans.append([arr[start], arr[end]])
    
    if abs(sumV - M) < minV:
        minV = abs(sumV - M)
        ans = [[arr[start], arr[end]]]

    if sumV - M < 0:
        start += 1
    else:
        end -= 1

for i in ans:
    print('{} {}'.format(i[0], i[1]), end=' ')