import sys
sys.stdin = open('5178.txt')

T = int(input())
for t in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N + 1)]
    for m in range(M):
        leaf, value = map(int, input().split())
        tree[leaf] = value
    
    while N > 1:
        if not N % 2: # N 이 짝수, 형제노드가 없을 때
            tree[N // 2] = tree[N]
            N -= 1

        tree[N // 2] = tree[N] + tree[N - 1]
        N -= 2
    
    print('#{} {}'.format(t, tree[L]))