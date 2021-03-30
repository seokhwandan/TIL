from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.db.models import Count, Q
import random
from django.views.decorators.http import require_http_methods, require_POST, require_safe
# Create your views here.

@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')

    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    # article = get_object_or_404(Article, pk=pk)
    # count1 = article.comment_set.filter(pick=1).count()
    # count2 = article.comment_set.filter(pick=2).count()
    # total = count1 + count2
    # if total == 0:
    #     per1 = 0
    #     per2 = 0
    # else:
    #     per1 = round(count1 / total * 100, 2)
    #     per2 = round(count2 / total * 100, 2)

    comment_form = CommentForm(pk)
    total = Count('comment')
    count1 = Count('comment', filter=Q(comment__pick=1))
    count2 = Count('comment', filter=Q(comment__pick=2))

    result = Article.objects.annotate(
        total = total,
        count1 = count1,
        count2 = count2,
    )

    article = get_object_or_404(result, pk=pk)
    comments = article.comment_set.all()
    
    per1 = round(article.count1 / article.total * 100, 2) if article.total else 0
    per2 = round(article.count2 / article.total * 100, 2) if article.total else 0

    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
        'per1': per1,
        'per2': per2,
        'count1': article.count1,
        'count2': article.count2,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def comments_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm(pk, request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)

@require_safe
def random_detail(request):
    max_id = Article.objects.order_by('-pk')[0].id
    random_id = random.randint(1, max_id)
    return redirect('articles:detail', random_id)