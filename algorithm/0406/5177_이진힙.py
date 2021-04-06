import sys
sys.stdin = open('5177.txt')

def push(v):
    global cnt
    cnt += 1
    heap[cnt] = v
    c = cnt
    p = c // 2

    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]

        c = p
        p = c // 2

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    temp = list(map(int, input().split()))
    heap = [0] * (N + 1)
    cnt = 0

    for i in range(N):
        push(temp[i])
    
    n = N // 2
    ans = 0
    while n:
        ans += heap[n]
        n //= 2
    print('#{} {}'.format(t, ans))