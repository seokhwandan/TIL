import sys
sys.stdin = open('5174.txt')

def inorder(node):
    global cnt
    if node != 0:
        inorder(left[node])
        cnt += 1
        inorder(right[node])

T = int(input())
for t in range(1, T + 1):
    E, N = map(int, input().split())
    temp = list(map(int, input().split()))
    left = [0] * (E + 2)
    right = [0] * (E + 2)
    for i in range(E):
        p = temp[i * 2] # 부모
        c = temp[i * 2 + 1] # 자식
        if left[p]: # 왼쪽 값이 있으면
            right[p] = c
        else: # 없으면
            left[p] = c
    cnt = 0
    inorder(N)
    print('#{} {}'.format(t, cnt))