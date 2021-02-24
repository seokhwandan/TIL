arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
sel = [0] * N

# {1, 2, 3} 부분집합
import time

start = time.time()
arr = [n for n in range(1, 301)]
N = len(arr)
A = [0] * N  # 원소의 포함 여부를 저장

# 완전검색 dfs를 재귀로 만든 후, 가지치기 = 백트래킹
cnt = 0


def powerset(n, k):  # n: 원소의 갯수, k: 현재 depth 
    global cnt
    # 가지치기
    # 음 powerset(n, k + 1)들을 실행을 안해서 빨라지나?
    total = 0
    for i in range(N):
        if A[i]:
            total += arr[i]
    if total > 10:
        return

    if n == k:  # basis part
        # 계산: 부분집합의 합 등 솔루션을 구하는 부분
        tmp = 0
        for i in range(N):
            if A[i]:
                tmp += (arr[i])

        if tmp == 10:
            cnt += 1
            for i in range(N):
                if A[i]:
                    print(arr[i], end=' ')
            print()


    else:  # inductive part
        A[k] = 1
        powerset(n, k + 1)  # 깊이가 증가하는 방향으로 유도
        A[k] = 0
        powerset(n, k + 1)


powerset(N, 0)
print(cnt)

end = time.time()

print(end - start)