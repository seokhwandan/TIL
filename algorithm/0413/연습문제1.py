#  0,120,12,7,76,24,60,121,124,103

arr = [0,0,0,0,0,0,0,1,1,1,  1,0,0,0,0,0,0,1,1,0,  0,0,0,0,0,1,1,1,1,0, 0,1,1,0,0,0,0,1,1,0,  0,0,0,1,1,1,1,0,0,1,  1,1,1,0,0,1,1,1,1,1,  1,0,0,1,1,0,0,1,1,1]

for i in range(0, len(arr), 7):
    res = ''
    if i + 7 < len(arr):
        for j in range(i, i + 7):
            res += str(arr[j])
    else:        
        for j in range(i, len(arr)):
            res += str(arr[j])

    ans = 0
    for k in range(len(res)):
        ans += int(res[k]) * (2 ** (len(res) - 1 - k))
    print(ans, end=' ')