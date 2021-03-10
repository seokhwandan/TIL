Create, Read, Update, Delete



django-admin startproject crud

python manage.py startapp articles

- crud/settings.py 에서 INSTALLED_APPS 에 articles 추가

- articles/models.py에서 Article 클래스 생성, (models.Model) 을 반드시 상속받아야 함 

  ```python
  class Article(models.Model):
      # 필드 정의
      # CharField 는 길이 제한이 있고, TextField 는 길이 제한이 없음
      title = models.CharField(max_length=100)
      content = models.TextField()
  ```

  

python manage.py makemigrations

python manage.py migrate

pip install django-extensions

- 장고의 확장프로그램 설치
- crud/settings.py 에서 INSTALLED_APPS 에 django_extensions 추가

python manage.py shell_plus

- exit

- articles/models.py에서 Article 클래스 내용 추가

  ```python
  class Article(models.Model):
      # 필드 정의
      # CharField 는 길이 제한이 있고, TextField 는 길이 제한이 없음
      title = models.CharField(max_length=100)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```

python manage.py makemigrations

python manage.py migrate

python manage.py sehll_plus

```
article = Article()
article.title = ''
article.content = ''
article.save()

article = Article(title='', content='')
article.save()

Article.objects.creat(title='', content='')
create 하는 방법 3가지	
```



articles/admin.py

- from .models import Article
- admin.site.register(Article)

python manage.py createsuperuser



articles/admin.py (admin page 확인)

```python
def ArticleAdmin(admin.ModelAdmin):
	list_display = ('pk', 'title', 'content', 'created_at', 'updated_at')
admin.site.register(Article, ArticleAdmin)
```

