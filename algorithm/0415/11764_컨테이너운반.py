import sys
sys.stdin = open('11764.txt')

T = int(input())
for tc in range(1, T + 1):
    arr = []
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    T = list(map(int, input().split()))
    W.sort(reverse=True)
    T.sort(reverse=True)
    arr.append(T)
    arr.append(W)
    check_t = [0] * M
    check_w = [0] * M
    
    res = []
    for t in range(M):
        for w in range(N):
            if arr[0][t] >= arr[1][w] and not check_t[t] and not check_w[w]:
                res.append(arr[1][w])
                check_t[t] = 1
                check_w[w] = 1
    print('#{} {}'.format(tc, sum(res)))