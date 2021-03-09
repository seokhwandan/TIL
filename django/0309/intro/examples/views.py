from django.shortcuts import render
from datetime import datetime

# Create your views here.

def dtl_practice(request):
    foods = ['짜장면', '탕수육', '짬뽕', '칠리새우', '크림새우']
    fruits = ['apple', 'banana', 'cucumber', 'mango']
    user_list = []
    my_sentence = 'abcde fghij klmn'
    date_time = datetime.now()
    context = {
        'foods': foods,
        'fruits': fruits,
        'user_list': user_list,
        'my_sentence': my_sentence,
        'date_time': date_time,
    }
    return render(request, 'examples/dtl_practice.html', context)

def index(request):
    return render(request, 'examples/index.html')

def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'examples/hello.html', context)