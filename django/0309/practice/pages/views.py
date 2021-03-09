from django.shortcuts import render
import requests
import random

# Create your views here.

def fake_google(request):
    return render(request, 'pages/fake_google.html')

def calc(request, n1, n2):
    cal = []
    plus = '덧셈 : ' + str(n1 + n2)
    cal.append(plus)
    minus = '뺄셈 : ' + str(n1 - n2)
    cal.append(minus)
    mul = '곱셈 : ' + str(n1 * n2)
    cal.append(mul)
    div = '나눗셈 : ' + str(n1 / n2)
    cal.append(div)
    context = {
        # 'plus': plus,
        # 'minus': minus,
        # 'mul': mul,
        # 'div': div,
        'cal': cal,
    }
    return render(request, 'pages/calc.html', context)

def lotto(request):
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=953"
    res = requests.get(url).json()
    num = []
    No = ''
    for i in range(1, 7):
        No = 'drwtNo' + str(i)
        num.append(res[No])
    bonus = res['bnusNo']

    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    l = 0
    number = list(range(1, 46))
    while l < 1000:
        cnt = 0
        pick = random.choices(number, k=6)
        for i in num:
            if i in pick:
                cnt += 1
        if cnt == 6:
            a += 1
        elif cnt == 5:
            if bonus in pick:
                b += 1
            else:
                c += 1
        elif cnt == 4:
            d += 1
        elif cnt == 3:
            e += 1
        else:
            f += 1
        l += 1
    context = {
        'num': num,
        'bonus': bonus,
        '1등': a,
        '2등': b,
        '3등': c,
        '4등': d,
        '5등': e,
        '꽝': f,
    }
    return render(request, 'pages/lotto.html', context)