import sys
sys.stdin = open('4843.txt')

T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=' ')
    N = int(input())
    num = list(map(int, input().split()))
    arr = [0] * N

    for i in range(len(num) - 1):
        min_idx = i
        for j in range(i + 1, len(num)):
            if num[min_idx] > num[j]:
                min_idx = j
        num[i], num[min_idx] = num[min_idx], num[i]

    idx = 1
    while idx <= len(arr) - 1:
        for n in range(len(num) // 2):
            arr[idx] = num[n]
            idx += 2
    
    idx = 0
    while idx <= len(arr) - 1:
        for n in range(len(num) - 1, len(num) // 2 - 1, - 1):
            arr[idx] = num[n]
            idx += 2

    if len(arr) > 10:
        arr = arr[:10]
    print(*arr)
