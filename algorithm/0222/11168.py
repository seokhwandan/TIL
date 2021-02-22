import sys
sys.stdin = open('11168.txt')

T = int(input())
for t in range(1, T + 1):
    print(f'#{t}')
    H, W  = map(int, input().split())
    res = [[0] * W for _ in range(H)]
    for w in range(W):
        for h in range(H):
            res[h][w] += h + H * w + 1
    
    for i in range(len(res)):
        result = ''
        for j in range(len(res[i])):
            result += str(res[i][j]) + ' '
        print(result)