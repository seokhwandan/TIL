import sys
sys.stdin = open('5176.txt')

def inorder(node):
    global cnt
    if node <= N:
        inorder(node * 2)
        tree[node] = cnt
        cnt += 1
        inorder(node * 2 + 1)

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    tree = [0 for _ in range(N + 1)]
    cnt = 1
    inorder(1)
    print('#{} {} {}'.format(t, tree[1], tree[N//2]))