## DFS 알고리즘 - 재귀

```python
DFS_Recursive(G, v)
	visited[ v ] <- TRUE // v 방문 설정
    
    FOR each all w in adjacency(G, v)
    	IF visited[w] != TRUE
        	DFS_Recuresive(G, w)
```

