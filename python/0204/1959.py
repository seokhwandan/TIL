import sys
sys.stdin = open('1959.txt')

T = int(input())

for t in range(1, T + 1):
    print(f'#{t}', end=' ')
    N, M = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for v in range(2)]
    Ai = AB[0] # N
    Bj = AB[1] # M
    result = []
    for i in range(abs(N-M) + 1):
        res = 0
        if N > M:
            for m in range(M):
                res += Ai[i + m] * Bj[m]
                # print(Ai[i + m] * Bj[m])
        else:
            for n in range(N):
                res += Ai[n] * Bj[i + n]
                # print(Ai[n] * Bj[i + n])
        result.append(res)
    print(max(result))