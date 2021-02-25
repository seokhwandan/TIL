import sys
sys.stdin = open('2805.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    tmp = [list(map(int, input())) for _ in range(N)]
    profit = 0
    # print(tmp)
    for i in range(N):
        if i < N // 2:
            profit += sum(tmp[i][N // 2 - i:-(N // 2 - i)])
        elif i == N // 2:
            profit += sum(tmp[i][:N + 1])
        else:
            profit += sum(tmp[i][i - N // 2:-(i - N // 2)])
    print('#{} {}'.format(t, profit))