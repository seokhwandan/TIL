import sys
sys.stdin = open('1231.txt')

def inorder(node):
    global ans
    # 왼쪽, 오른쪽 자식이 둘다 있을 때
    if len(temp[node]) == 4:
        # inorder(int(temp[node][2]) - 1)
        inorder(int(temp[node][2]))
        ans += temp[node][1]
        # inorder(int(temp[node][3]) - 1)
        inorder(int(temp[node][3]))
    
    # 자식이 하나일 때
    elif len(temp[node]) == 3:
        # inorder(int(temp[node][2]) - 1)
        inorder(int(temp[node][2]))
        ans += temp[node][1]

    # 자식이 없을 때
    else:
        ans += temp[node][1]
    

for t in range(1, 11):
    V = int(input())
    # temp = [list(map(str, input().split())) for _ in range(V)]
    # 1부터 시작하므로 맨 앞에 0 추가
    temp = [[0]] + [list(input().split()) for _ in range(V)]
    ans = ''
    # inorder(0)
    inorder(1)
    print('#{} {}'.format(t, ans))