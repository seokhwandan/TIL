## 문자열을 숫자열로 변환

```python
def atoi(num_str):
	
	# 최종 값을 담을 변수
    value = 0
    
    for i in range(len(num_str)):
        value *= 10
        value += ord(num_str[i]) - ord('0')
        print(vlaue)
        
	return value
```



## 고지식한 패턴 검색 알고리즘

```python
p = 'is' # 찾을 패턴
t = 'This is a book~!' # 전체 택스트
M = len(p) # 찾을 패턴의 길이
N = len(t) # 전체 텍스트의 길이

def BruteForce(p, t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == M:
        return i - M # 검색 성공
    else:
        return -1 # 검색 실패
```

