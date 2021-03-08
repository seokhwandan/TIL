arr = [1, 2, 3] # 우리가 활용할 데이터
N = len(arr)
sel = [0] * N # 결과들이 저장될 리스트
check = [0] * N # 해당 원소를 이미 사용했는지 안했는지에 대한 체크

# 재귀
def perm(idx):
    if idx == N:
        print(sel)
    else:
        for i in range(N):
            if check[i] == 0:
                sel[idx] = arr[i] # 값을 써라
                check[i] = 1 # 사용을 했다는 표시
                perm(idx + 1) 
                check[i] = 0 # 다음 반복문을 위한 원상복구
perm(0)

# 비트
# ch = check 10 진수 정수
def perm1(idx, ch):
    if idx == N:
        print(sel)
        return
    
    for i in range(N):
        # j 번째 원소를 활용을 했으니, 쓰지 않는다.
        if ch & (1 << i):
            continue
        sel[idx] = arr[i]
        perm1(idx + 1, ch | (1 << i)) # ch 가 1회성으로 활용되기 때문에 원상복구가 필요없다.

# perm1(0, 0)

#스왑
def perm2(idx):
    if idx == N:
        print(arr)
    else:
        for i in range(idx, N):
            # 순서를 바꾸고
            arr[idx], arr[i] = arr[i], arr[idx]
            perm2(idx + 1)
            # 원상복귀
            arr[idx], arr[i] = arr[i], arr[idx]