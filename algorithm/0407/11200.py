import sys
sys.stdin = open('11200.txt')

T = int(input())
for t in range(1, T + 1):
    print(f'#{t}')
    N, M = map(int, input().split())
    for n in range(1, N + 1):
        if M == 1:
            if n <= 3:
                print('*' * n)
            else:
                print('*' * (N - n + 1))
        elif M == 2:
            if n <= 3:
                print(' ' * (N - n - 2) + '*' * n)
            else:
                print(' ' * (n - N + 2) + '*' * (N - n + 1))
        elif M == 3:
            if n <= 3:
                print(' ' * (n - 1) + '*' * (2 * (N - n - 1) - 1))
            else:
                print(' ' * (N - n) + '*' * (2 * (n - N + 3) - 1))
        else:
            if n <= 3:
                print(' ' * (n - 1) + '*' * (N - n - 1))
            else:
                print(' ' * 2 + '*' * (n - 2))
