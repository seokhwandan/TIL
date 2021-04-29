import sys
sys.stdin = open('12100.txt')

from copy import deepcopy

def find_maxV(arr): # 최대값 찾기
    global maxV
    for i in range(N):
        for j in range(N):
            maxV = max(maxV, arr[i][j])

def moveL(arr):
    for i in range(N): # row
        val = 0 
        move = 0 # 가장 왼쪽
        for j in range(N): # column
            if arr[i][j]: # 값이 있으면
                if not val: # val가 0, 즉 이전 블록이 없다
                    val = arr[i][j]
                else: # val가 있으면, 즉 이전 블록의 값이 있다면
                    if val == arr[i][j]: # 이동할 블럭과 값이 같다면
                        arr[i][move] = val * 2 # 이동할 곳에 값 * 2
                        move += 1 # 가장 왼쪽이 채워졌으므로 한칸 이동
                        val = 0 # 값 초기화
                    else: # 이동할 블럭과 값이 다르다면
                        arr[i][move] = val # 이동할 블럭에 값 저장
                        val = arr[i][j] # 값 갱신
                        move += 1 # 한칸 이동
                arr[i][j] = 0 # 블럭을 이동했으므로 블럭 비우기
            if val: # 이동할 블럭이 있다면
                arr[i][move] = val
    return arr

def moveR(arr):
    for i in range(N):
        val = 0
        move = N - 1
        for j in range(N - 1, -1, -1):
            if arr[i][j]:
                if not val:
                    val = arr[i][j]
                else:
                    if val == arr[i][j]:
                        arr[i][move] = val * 2
                        move -= 1
                        val = 0
                    else:
                        arr[i][move] = val
                        val = arr[i][j]
                        move -= 1
                arr[i][j] = 0
            if val:
                arr[i][move] = val
    return arr    

def moveU(arr):
    for i in range(N):
        val = 0
        move = 0
        for j in range(N):
            if arr[j][i]:
                if not val:
                    val = arr[j][i]
                else:
                    if val == arr[j][i]:
                        arr[move][i] = val * 2
                        move += 1
                        val = 0
                    else:
                        arr[move][i] = val
                        val = arr[j][i]
                        move += 1
                arr[j][i] = 0
            if val:
                arr[move][i] = val
    return arr

def moveD(arr):
    for i in range(N):
        val = 0
        move = N - 1
        for j in range(N - 1, -1, -1):
            if arr[j][i]:
                if not val:
                    val = arr[j][i]
                else:
                    if val == arr[j][i]:
                        arr[move][i] = val * 2
                        move -= 1
                        val = 0
                    else:
                        arr[move][i] = val
                        val = arr[j][i]
                        move -= 1
                arr[j][i] = 0
            if val:
                arr[move][i] = val
    return arr    

def f(arr, n):
    if n == 5:
        find_maxV(arr)
        return
    
    f(moveL(deepcopy(arr)), n + 1)
    f(moveR(deepcopy(arr)), n + 1)
    f(moveU(deepcopy(arr)), n + 1)
    f(moveD(deepcopy(arr)), n + 1)

N = int(input())
game = [list(map(int, input().split())) for _ in range(N)]
maxV = 0
f(game, 0)
print(maxV)