import sys
sys.stdin = open('5205.txt')

# def quick_sort(arr, left, right):
#     if left < right:
#         p = partition(arr, left, right)
#         quick_sort(arr, left, p - 1)
#         quick_sort(arr, p + 1, right)

# def partition(arr, left, right):
#     pivot = (left + right) // 2

#     while left < right :
#         while(arr[left] < arr[pivot] and left < right):
#             left += 1
#         while(arr[right] >= arr[pivot] and left < right):
#             right -= 1

#         if left < right:
#             if left == pivot:
#                 pivot = right
#             arr[left], arr[right] = arr[right], arr[left]

#     arr[pivot], arr[right] = arr[right], arr[pivot]
#     return right

# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     quick_sort(arr, 0, N - 1)
#     print('#{} {}'.format(t, arr[N // 2]))

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

def quick_sort(arr, start, end):
    pivot = partition(arr, start, end)

    if start < pivot - 1:
        quick_sort(arr, start, pivot - 1)

    if end > pivot:
        quick_sort(arr, pivot + 1, end)

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, N - 1)
    print('#{} {}'.format(t, arr[N // 2]))