import sys
sys.stdin = open('5099.txt')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    q = []
    for i in range(N):
        q.append([pizza[i], i + 1])
    
    i = 0
    while len(q) != 1:
        q[0][0] //= 2
        if not q[0][0]:
            if N + i < M:
                q.pop(0)
                q.append([pizza[N + i], N + i + 1])
                i += 1
            else:
                q.pop(0)
        else:
            q.append(q.pop(0))
    print('#{} {}'.format(t, q[0][1]))