import sys
sys.stdin = open('1231.txt')

def inorder(node):
    if node <= V:
        inorder(node * 2)
        print(tree[node], end='')
        inorder(node * 2 + 1)


for t in range(1, 11):
    V = int(input())
    tree = [0 for _ in range(V + 1)]
    for i in range(V):
        temp = input().split()
        tree[int(temp[0])] = temp[1]
    
    print('#{}'.format(t), end=' ')
    inorder(1)
    print()