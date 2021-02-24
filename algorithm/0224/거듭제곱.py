def Recursive_Power(x, n):
    if n == 1:
        return x
    if n % 2 == 0:
        y = Recursive_Power(x, n // 2)
        return y * y
    else:
        y = Recursive_Power(x, (n - 1) // 2)
        return y * y * x

print(Recursive_Power(2, 300000))