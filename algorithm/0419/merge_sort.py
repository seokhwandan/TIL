# 방법 1
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


# 방법 2
def partition(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst)//2
    left_lst = partition(lst[:mid])
    right_lst = partition(lst[mid:])
    return merge(left_lst, right_lst)


def merge(left_lst, right_lst):
    global cnt
    result = []

    while len(left_lst) > 0 or len(right_lst) > 0:
        if len(left_lst) > 0 and len(right_lst) > 0:
            if left_lst[0] <= right_lst[0]:
                result.append(left_lst[0])
                left_lst = left_lst[1:]
            else:
                result.append(right_lst[0])
                right_lst = right_lst[1:]

        elif len(left_lst) > 0:
            result.append(left_lst[0])
            left_lst = left_lst[1:]
        elif len(right_lst) > 0:
            result.append(right_lst[0])
            right_lst = right_lst[1:]

    return result