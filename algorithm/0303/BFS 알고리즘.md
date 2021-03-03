## BFS 알고리즘

- ### 입력 파라미터 : 그래프 G와 탐색 시삭점 v

  ```python
  def BFS(G, v): # 그래프 G, 탐색 시작점 v
      visited = [0] * n # n : 정점의 갯수
      queue = [] # 큐 생성
      queue.append(v) # 시작점 v를 큐에 삽임
      while queue: # 큐가 비어있지 않은 경우
          t = queue.pop(0) # 큐의 첫번째 원소 반환
          if not visited[t]: # 방문되지 않은 곳이라면
              visited[t] = True # 방문한 것으로 표시
              visit(t)
          for i in G[t]: # t와 연결된 모든 선에 대해
              if not visited[i]: # 방문되지 않은 곳이라면
                  queue.append(i) # 큐에 넣기
  ```




- 입력 파라미터 : 그래프 G와 탐색 시작점 v (enQ시 방문처리)

  ```python
  def BFS(G, v): # 그래프 G, 탐색 시작점 v
      visited = [0] * (n + 1) # n : 정점의 갯수
      q = [] # 큐 생성
      
      q.append(v) # 시작점 v 를 enQueue
      visited[v] = 1 # 방문한 것으로 표시
      
      while q: # 큐가 비어있지 않은 경우
          t = q.pop(0) # deQueue(왼쪽 원소 반환)
          for w in G[t]: # 정점 t와 인접한 정점 w에 대해
              if not visited[w]: # 방문하지 않은 곳이라면
                  q.append(w) # enQueue
                  visited[w] = visited[t] + 1 # 방문한 것으로 표시
  ```

  