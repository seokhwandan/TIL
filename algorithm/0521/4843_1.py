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
        max_idx = i
        for j in range(i + 1, len(num)):
            if i % 2:
                if num[min_idx] > num[j]:
                    min_idx = j
            else:
                num[i] = 0
        num[i], num[min_idx] = num[min_idx], num[i]
    print(num)
