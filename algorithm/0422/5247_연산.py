import sys
sys.stdin = open('5247.txt')

from collections import deque

def solve(n, m):
    global ans

    while q:
        num, cnt = q.popleft()

        if num == m:
            ans = min(ans, cnt)
            return ans
        
        if ans < cnt:
            return

        if 0 < num + 1 <= 1000000 and not visited[num + 1]:
            q.append((num + 1, cnt + 1))
            visited[num + 1] = 1

        if 0 < num - 1 <= 1000000 and not visited[num - 1]:
            q.append((num - 1, cnt + 1))
            visited[num - 1] = 1

        if 0 < num * 2 <= 1000000 and not visited[num * 2]:
            q.append((num * 2, cnt + 1))
            visited[num * 2] = 1

        if 0 < num - 10 <= 1000000 and not visited[num - 10]:
            q.append((num - 10, cnt + 1))
            visited[num - 10] = 1


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    q = deque()
    visited = [0] * 1000001
    q.append((N, 0))
    visited[N] = 1
    ans = 9999999
    solve(N, M)
    print('#{} {}'.format(t, ans))