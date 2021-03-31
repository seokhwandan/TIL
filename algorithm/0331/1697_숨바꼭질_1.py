from collections import deque

def f(k):
    
    while q:
        t, d = q.popleft()
        if t == k:
            return d
        
        visited[t] = 1
        if t - 1 >= 0 and not visited[t - 1]:
            q.append([t - 1, d + 1])
        if t + 1 <= 100000 and not visited[t + 1]:
            q.append([t + 1, d + 1])
        if t * 2 <= 100000 and not visited[t * 2]:
            q.append([t * 2, d + 1])

n, k = map(int, input().split())
# n, k = 5, 17
visited = [0] * 100001
q = deque()
q.append([n, 0])
print(f(k))