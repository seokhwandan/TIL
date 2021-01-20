for i in range(5):
    s = ''
    for j in range(5):
        if i == j:
            s += '#'
        else:
            s += '+'
    print(s)