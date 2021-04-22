import sys
sys.stdin = open('5249.txt')

def find(n):
    if n == p[n]:
        return n
    else:
        return find(p[n])

def union(s, e):
    n1, n2 = find(s), find(e)
    if n1 > n2:
        p[n1] = n2
    else:
        p[n2] = n1
        
T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    arr.sort(key=lambda x: x[2])
    p = list(range(V + 1))

    ans = cnt = 0
    for s, e, d in arr:
        if find(s) != find(e):
            union(s, e)
            ans += d
            cnt += 1

        if cnt == V:
            break
    
    print('#{} {}'.format(t, ans))