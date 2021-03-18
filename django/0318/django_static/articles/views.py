from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)


# def create(request):
#     # 값을 받아서 폼 인스턴스 생성
#     form = ArticleForm(request.POST)

#     # 유효성 검사
#     if form.is_valid():
#         # DB에 저장 (Form 으로 작성했을 때)
#         # title = form.cleaned_data.get('title')
#         # content =form.cleaned_data.get('content')
#         # article = Article(title=title, content=content)
#         # article.save()

#         # DB에 저장 (Model Form 으로 작성했을 때)
#         article = form.save() # 저장된 데이터의 인스턴스를 return 한다

#         return redirect('articles:index')
    
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)


def create(request):
    if request.method == "POST":
        # def create : DB 에 저장하는 동작
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)

    else:
        # def new : page 를 보여주는 동작 (new 는 GET 으로 요청하기 때문에)
        form = ArticleForm()

    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def edit(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article) # instance 로 article 을 받아와야 기존의 값을 수정할 수 있다.
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)

    else:
        form = ArticleForm(instance=article) # article 정보로 form을 생성해 준다.

    context = {
        'form': form,
        'article':article,
    }
    return render(request, 'articles/edit.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')

    return redirect('articles:detail', article.pk)