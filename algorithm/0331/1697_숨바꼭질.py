from collections import deque

def f(k):
    while q:
        t, d = q.popleft() # t = 출발위치, d = 이동시간
        if t == k: # 목적지에 도착 시 이동시간 리턴
            return d
        
        visited[t] = 1 # 방문체크 
        for nt in (t - 1, t + 1, t * 2): # 이동할 수 있는 위치에 순회
            if 0 <= nt <= 100000 and not visited[nt]: # 범위 내에서 방문한 적이 없을 경우
                q.append([nt, d + 1]) # 다음위치와 이동시간 + 1 enQueue

n, k = map(int, input().split())
# n, k = 5, 17
visited = [0] * 100001 # 방문체크
q = deque()
q.append([n, 0]) # 출발위치와 이동시간 enQueue
print(f(k))