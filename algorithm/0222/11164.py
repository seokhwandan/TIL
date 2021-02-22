import sys
sys.stdin = open('11164.txt')

T = int(input())
for t in range(1, T + 1):
    print(f'#{t}')
    H, W  = map(int, input().split())
    for h in range(H):
        res = []
        if h % 2:
            for w in range(W, 0, -1):
                res.append(w + W * h)
        else:
            for w in range(1, W + 1):
                res.append(w + W * h)
        print(*res)