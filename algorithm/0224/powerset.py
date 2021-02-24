arr = [1, 2, 3] # 우리가 활용할 데이터
N = len(arr)
sel = [0] * N # a 리스트(내가 해당 원소를 뽑았는지 체크) / 원소의 포함 여부를 저장

def powerset(idx):
    if idx == N:
        print(sel, ':', end=' ')
        for i in range(N):
            if sel[i]:
                print(arr[i], end=' ')
        print()
        
        return
    
    # idx 자리의 원소를 뽑고 간다.
    sel[idx] = 1
    powerset(idx + 1)
    # idx 자리를 안뽑고 간다.
    sel[idx] = 0
    powerset(idx + 1)

powerset(0)

A = [0] * N
def powerset1(n, k):
    if n == k: # n : 원소의 갯수, k : 현재 depth
        # 솔루션 구하기
        print(A)
    else:
        A[k] = 1
        powerset1(n, k + 1)
        A[k] = 0
        powerset1(n, k + 1)

powerset1(N, 0)

