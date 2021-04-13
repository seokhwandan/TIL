# temp = '0F97A3'
temp = '01D06079861D79F99F'

dic = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
}

binD = ''
for i in temp:
    binD += dic[i]

for i in range(0, len(binD), 7):
    res = ''
    if i + 7 < len(binD):
        for j in range(i, i + 7):
            res += binD[j]
    else:        
        for j in range(i, len(binD)):
            res += binD[j]
    
    ans = 0
    for k in range(len(res)):
        ans += int(res[k]) * (2 ** (len(res) - 1 - k))
    print(ans, end=' ')