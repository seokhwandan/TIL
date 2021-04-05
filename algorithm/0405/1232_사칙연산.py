import sys
sys.stdin = open('1232.txt')

def postorder(node):
    if tree[node][1] == 0:
        return tree[node][0]

    lv = postorder(tree[node][1])
    rv = postorder(tree[node][2])
    
    if tree[node][0] == '+':
        return lv + rv
    if tree[node][0] == '-':
        return lv - rv
    if tree[node][0] == '*':
        return lv * rv
    if tree[node][0] == '/':
        return lv // rv

for t in range(1, 11):
    V = int(input())
    tree = [[0] * 3 for _ in range(V + 1)]
    for i in range(1, V + 1):
        temp = input().split()
        if len(temp) > 2:
            tree[i][0] = temp[1]
            tree[i][1] = int(temp[2])
            tree[i][2] = int(temp[3])
        else:
            tree[i][0] = int(temp[1])
    print('#{} {}'.format(t, postorder(1)))
