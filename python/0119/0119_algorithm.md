## SWEA (#2027)

주어진 텍스트를 그대로 출력하세요.

```
#++++
+#+++
++#++
+++#+
++++#
```

> solve

```python
for i in range(5):
    s = ''
    for j in range(5):
        if i == j:
            s += '#'
        else:
            s += '+'
    print(s)
```



## SWEA (#2029)

2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.

> solve

```python
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(T):
    num = list(map(int, input().split(" ")))

    n1, n2 = num
    print('#{} {} {}'.format(t+1, n1 // n2, n1 % n2))
```



## SWEA (#1545)

주어진 숫자부터 0까지 순서대로 찍어보세요.

```python
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T, -1, -1):
    print(t, end=' ')
```

