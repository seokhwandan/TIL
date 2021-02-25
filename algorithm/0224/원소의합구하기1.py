arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
sel = [0] * N

# {1, 2, 3} 부분집합
import time

start = time.time()
arr = [n for n in range(1, 301)]
N = len(arr)
A = [0] * N  # 원소의 포함 여부를 저장

cnt = 0
def powerset(n, k, cursum):  # n: 원소의 갯수, k: 현재 depth, cursum : 부분집합의 합
    global cnt
    # 가지치기
    if cursum > 10:
        return

    if n == k:
        # 솔루션 구하기
        # 합이 10일 때 카운트 증가
        if cursum == 10:
            cnt += 1
            for i in range(N):
                if A[i]:
                    print(arr[i], end=' ')
            print()

    else:
        A[k] = 1
        powerset(n, k + 1, cursum + arr[k])
        A[k] = 0
        powerset(n, k + 1, cursum)


powerset(N, 0, 0)
print(cnt)

end = time.time()

print(end - start)ㅈ