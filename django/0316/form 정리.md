##### articles 에 froms.py 생성

- form은 유저로부터 데이터를 입력받는 값만 정의한다.

##### forms.py

```python
from django import forms

class ArticleForm(forms.Form):
	title = forms.CharField(max_length=10)
	content = forms.CharField(widget=forms.Textarea)
```

##### 

##### new.html

```django
{% extends 'base.html' %}
{% block content %}
<h2>NEW</h2>
<hr>
<form action="{% url 'articles:create' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <button>글작성</button>
</form>
{% endblock content %}
```



##### views.py

```python
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)


def create(request):
    # 값을 받아서 폼 인스턴스 생성
    form = ArticleForm(request.POST)

    # 유효성 검사
    if form.is_valid():
        # DB에 저장
        title = form.cleaned_data.get('title')
        content =form.cleaned_data.get('content')
        article = Article(title=title, content=content)
        article.save()
        return redirect('articles:index')
    
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```





#### Model Form

##### forms.py

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # 메타 데이터를 저장하는 class
    class Meta:
        model = Article
        # 원하는 필드만 입력받을 경우
        # field = ('title', 'content')
        # 모든 필드를 입력받고 싶은 경우
        fields = '__all__'
```



##### views.py

```python
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)


def create(request):
    # 값을 받아서 폼 인스턴스 생성
    form = ArticleForm(request.POST)

    # 유효성 검사
    if form.is_valid():
        # DB에 저장 (Model Form 으로 작성했을 때)
        article = form.save() # 저장된 데이터의 인스턴스를 return 한다

        return redirect('articles:index')
    
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```



#### new 와 create 합치기 !!!

```python
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def create(request):
    if request.method == "POST":
        # def create : DB 에 저장하는 동작
        form = ArticleForm(request.POST)
        
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')

    else:
        # def new : page 를 보여주는 동작 (new 는 GET 으로 요청하기 때문에)
        form = ArticleForm()

    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```



#### edit 과 update 합치기 !!!

##### edit.html

```django
{% extends 'base.html' %}
{% block content %}
<h2>EDIT</h2>
<form action="" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <button>수정</button>
  <br>
  <a href="{% url 'articles:detail' article.pk %}">BACK</a>
</form>
{% endblock content %}
```



##### views.py

```python
def edit(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        # instance 로 article 을 받아와야 기존의 값을 수정할 수 있다.
        form = ArticleForm(request.POST, instance=article) 
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
```



#### delete

- 삭제되므로 method 를 POST 로 받아야 한다.

  ##### detail.html

  ```django
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <button>DELETE</button>
    </form>
  ```

  ##### views.py

  ```python
  def delete(request, pk):
      article = Article.objects.get(pk=pk)
      if request.method == 'POST':
          article.delete()
          return redirect('articles:index')
  
      return redirect('articles:detail', article.pk)
  ```

  

#### form 꾸미기

```python
class ArticleForm(forms.ModelForm):
    # form 꾸미기
    title = forms.CharField(
        label="제목",
        widget=forms.TextInput(
            attrs={
                'class': 'my-title abc',
                'placeholder': "제목을 10자로 적어주세요.",
            }
        )
    )
    content = forms.CharField(
        label="내용",
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': '내용을 적어주세요.',
            }
        )
    )
   	class Meta:
        model = Article
        fields = '__all__'
```



