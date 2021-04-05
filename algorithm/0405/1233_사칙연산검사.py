import sys
sys.stdin = open('1233.txt')

def inorder(node):
    if node <= V:
        inorder(node * 2)
        stack.append(tree[node])
        inorder(node * 2 + 1)

def check(arr):
    m = len(arr) // 2
    for i in range(m):
        if arr[i * 2] in '+-*/':
            return 0
        if arr[i * 2 + 1] not in '+-*/':
            return 0
    return 1

for t in range(1, 11):
    V = int(input())
    tree = [0 for _ in range(V + 1)]
    stack = []
    for i in range(V):
        temp = input().split()
        tree[int(temp[0])] = temp[1]

    inorder(1)
    print('#{} {}'.format(t, check(stack)))