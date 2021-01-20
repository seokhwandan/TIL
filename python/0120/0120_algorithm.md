## SWEA (#1933)

입력으로 1개의 정수 N 이 주어진다.

정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.

```python
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

for n in range(1, N + 1):
	if N % n == 0:
        print(n, end=' ')
```



## SWEA (#1936)

A와 B가 가위바위보를 하였다.

가위는 1, 바위는 2, 보는 3으로 표현되며 A와 B가 무엇을 냈는지 입력으로 주어진다.

A와 B중에 누가 이겼는지 판별해보자. 단, 비기는 경우는 없다.

```python
import sys
sys.stdin = open('input.txt', 'r')

a, b = list(map(int, input().split()))

if a > b:
	print('A')
elif a == 1 and b == 3:
	print('A')
else:
	print('B')
```



## SWEA (#1938)

두 개의 자연수를 입력받아 사칙연산을 수행하는 프로그램을 작성하라.



[제약 사항]

1. 두 개의 자연수 a, b는 1부터 9까지의 자연수이다. (1 ≤ a, b ≤ 9)

2. 사칙연산 + , - , * , / 순서로 연산한 결과를 출력한다.

3. 나누기 연산의 결과에서 소수점 이하의 숫자는 버린다.

```python
import sys
sys.stdin = open('input.txt', 'r')

a, b = list(map(int, input().split()))
print(a + b)
print(a - b)
print(a * b)
print(a // b)
```

