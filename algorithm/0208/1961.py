import sys
sys.stdin = open('1961.txt')

T = int(input())

for t in range(1, T + 1):
    print(f'#{t}')
    N = int(input())
    test = [list(map(str, input().split())) for i in range(N)]
    # print(test)

    for h in range(N):
        sres1 = ''
        sres2 = ''
        sres3 = ''
        for v in range(N):
            # result[v][h]
            sres1 += test[N-1-v][h]
            sres2 += test[N-1-h][N-1-v]
            sres3 += test[v][N-1-h]

        print(sres1, sres2, sres3)