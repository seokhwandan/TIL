## 일반 백트래킹 알고리즘

```python
def checknode(v): #node
    if promising(v):
        if there is a solution at v:
            write the solution
        else:
            for u in each child of v:
                checknode(u)
```



## powerset을 구하는 백트래킹 알고리즘

```python
def backtrack(a, k, input): # a : 해당 원소를 사용 OX, k : index
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES
    
    if k == input:
        process_solution(a, k) # 답이면 원하는 작업을 한다
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

MAXCANDIDATES = 100
NMAX = 100
a = [0] * NMAX
backtrack(a, 0, 3)
```



## 퀵 정렬

```python
def partition(a, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while(a[L] < a[pivot] and L < R):
            L += 1
        while(a[R] >= a[pivot] and L < R):
            R -= 1
        if L < R:
            if L == pivot:
                pivot = R
                a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R
```

