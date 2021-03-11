## CREATE

1. 인스턴트를 생성해서 데이터를 일일히 넣은 후 저장해주는 방법
2. 인스턴스를 생성하면서 값도 같이 넣은 후 저장해주는 방법
3. 한줄로 작성하는 방법 `모델명.objects.create(필드=데이터, ...)`
   - save()가 필요하지 않다.
   - 리턴이 있따. 방금 저장된 인스턴스가 리턴된다.



## READ

1. 전체 정보를 가지고 오는 방법(all())
2. 하나의 정보만 가져오는 방법(get())
3. 특정 정보만 가져오는 방법(filter())
   - filed lookups



## UPDATE

- 기존에 있는 값을 가져와서 수정 후 다시 save()



## DELETE

- 삭제하려는 인스턴스 값을 가져와서 delete()



#### django-admin startproject crud

#### python manage.py startapp articles

- crud/settings.py 에서 INSTALLED_APPS 에 articles 추가

- articles/models.py에서 Article 클래스 생성, (models.Model) 을 반드시 상속받아야 함 

  ```python
  class Article(models.Model):
      # 필드 정의
      # CharField 는 길이 제한이 있고, TextField 는 길이 제한이 없음
      title = models.CharField(max_length=100)
      content = models.TextField()
  ```

  

#### python manage.py makemigrations

#### python manage.py migrate

#### pip install django-extensions

- 장고의 확장프로그램 설치
- crud/settings.py 에서 INSTALLED_APPS 에 django_extensions 추가

#### python manage.py shell_plus

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

#### python manage.py makemigrations

#### python manage.py migrate

#### python manage.py sehll_plus

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



#### articles/admin.py

- from .models import Article
- admin.site.register(Article)

python manage.py createsuperuser



articles/admin.py (admin page 확인)

```python
def ArticleAdmin(admin.ModelAdmin):
	list_display = ('pk', 'title', 'content', 'created_at', 'updated_at')
admin.site.register(Article, ArticleAdmin)
```

