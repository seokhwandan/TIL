import sys
sys.stdin = open('11172.txt')

T = int(input())
for t in range(1, T + 1):
    print(f'#{t}')
    HW = int(input())
    for h in range(HW):
        res = []
        for w in range(1, HW + 1):
            res.append(w + w * h)
        print(*res)