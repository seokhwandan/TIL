a = [1, 2, 3, 4]
n = len(a)

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            print(a[i], a[j], a[k])

# 3분할 n-1 comb 2
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        print(a[:i + 1], a[i + 1:j + 1], a[j + 1: n])