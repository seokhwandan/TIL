import sys
sys.stdin = open('5248.txt')

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
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    p = list(range(N + 1))

    for i in range(M):
        s, e = nums[i * 2], nums[i * 2 + 1]
        union(s, e)

    ans = set()
    for i in p:
        ans.add(find(i))
    
    print('#{} {}'.format(t, len(ans) - 1))