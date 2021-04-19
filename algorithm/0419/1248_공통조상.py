import sys
sys.stdin = open('1248.txt')

def find():
    global n1, n2

    ancestor = [] # 조상노드 list
    while n1: # n1 의 값이 0이 아닐 때 즉, 부모노드가 있을 때
        ancestor.append(parent[n1]) # 조상노드 list 에 부모노드 추가
        n1 = parent[n1] # n1 갱신
    
    while n2: # n2 의 값이 0이 아닐 때 즉, 부모노드가 있을 때
        if parent[n2] not in ancestor: # n1의 조상노드 list에 n2의 조상이 없다면
            n2 = parent[n2] # n2 갱신
        else: # 있다면
            return parent[n2] # 공통조상 반환


def sub_count(node):
    global cnt

    if node != 0:
        sub_count(left[node])
        cnt += 1
        sub_count(right[node])


T = int(input())
for t in range(1, T + 1):
    V, E, n1, n2 = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0

    left = [0] * (V + 1) # 왼쪽 자식 노드 list
    right = [0] * (V + 1) # 오른쪽 자식 노드 list
    parent = [0] * (V + 1) # 부모 노드 list
    for i in range(E):
        p = arr[i * 2] # 부모 
        c = arr[i * 2 + 1] # 자식

        if not left[p]: # 왼쪽 자식이 없으면
            left[p] = c # idx = 부모, value = 자식
        else: # 오른쪽 자식이 없으면
            right[p] = c # idx = 부모, value = 자식
        parent[c] = p # idx = 자식, value = 부모

    anc = find()
    sub_count(anc)
    print('#{} {} {}'.format(t, anc ,cnt))