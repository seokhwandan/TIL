import sys
sys.stdin = open('11197.txt')

T = int(input())
for t in range(1, T + 1):
    print(f'#{t}')
    N, M = map(int, input().split())
    if M == 1:
        for n in range(1, N + 1):
            print('*' * n)
    elif M == 2:
        for n in range(N, 0, -1):
            print('*' * n)
    else:
        for n in range(1, N + 1):
            print(f'{("*" * (2*n - 1)):^5}')