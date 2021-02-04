import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    print(f'#{N}')

    a = 0
    b = 1
    c = 0
    d = 0
    i = 1
    j = 0
    n = 1

    num = [[0 for i in range(N)] for j in range(N)]
    for literal in range(T):
        while j < N - a:
            num[a][j] = n - d
            j += 1
            n += 1
        while i < N - b:
            num[i + c][-b] = n - d
            i += 1
            n += 1
        while j > a:
            num[-b][j - 1] = n - a*2
            j -= 1
            n += 1
        while i > b:
            num[i - 1][a] = n - a*2
            i -= 1
            n += 1

        a += 1
        b += 1
        c = 1
        d = c+ a*2 - 2

    num[0][0] = 1
    for snail in num:
        print(*snail)