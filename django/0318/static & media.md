

## static files

- image, css, js 파일과 같이 내용이 고정되어, 응답 시 별도의 처리 없이 그대로 보여주는 파일

- 기본 static 경로

  - static / app_name / img, css, js / 파일저장

  - img, css, js 를 나누는 이유는 관리가 용이하기 때문



#### static 사용하기

```django
{% load static %}
<img src="{% static articles/sample.png %}" alt="sample">
```

- load static 이 없으면 사용할 수 없다.
- 경로를 입력해주어야 한다.



### The staticfiles app

- ##### STATIC_ROOT

  - Django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아넣는 경로

  - `collectstatic`이 배포를 위해 정적 파일을 수집하는 절대 경로

  - ##### collectstatic

    - 프로젝트 배포 시 흩어져 있는 정적 파일들을 모아 특정 디렉토리로 옮기는 작업

  - 개발 단계에서는 STATIC_ROOT 경로를 작성하지 않아도 문제없이 동작

    - 즉, 실제 서비스 배포 환경에서 필요한 경로

- ##### STATIC_URL
  - STATIC_ROOT에 있는 정적 파일을 참조 할 때 사용할 URL

    - 실제 파일이나 디렉토리가 아니고, URL로만 존재한다.

  - 비어 있지 않은 값으로 설정 하려면 반드시 slash(/)로 끝나야 함

    ```python
    STATIC_URL = '/static/'
    ```

- ##### STATICFILES_DIRS

  - app 내의 static 디렉토리 경로를 사용하는 것(기본 경로) 외에 추가적인 정적 파일 경로를 정의할 때 사용
  
    ```python
    STATICFILES_DIRS = BASE_DIR / 'assets'
    ```
  
    

## media

- 사용자가 웹에서 업로드 하는 모든 정적 파일

#### FileField, ImageField를 사용하기 위한 단계

1. settings.py 에 MEDIA_ROOT, MEDIA_URL 설정
2. upload_to 속성을 정의하여 업로드 된 파일에 사용할 MEDIA_ROOT 의 하위 경로 지정

3. 업로드 된 파일의 상대 URL 경로를 django 가 제공하는 url attribute 를 통해 사용 가능

- ##### MEDIA_ROOT

  - 사용자가 업로드 한 파일을 보관할 디렉토리의 절대 경로

  - 실제 해당 파일의 업로드가 끝나면 파일이 저장되는 경로

  - Django 는 성능을 위해 업로드 파일은 DB 에 저장하지 않음
    
    - DB 에 저장되는 것은 파일의 경로
    
  - MEDIA_ROOT 와 STATIC_ROOT 는 서로 다른 경로를 가져야 한다.

    ```python
    MEDIA_ROOT = BASE_DIR / 'upload_files' 
    ```

    ##### modes.py

    ```python
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    ```

    

- ##### MEDIA_URL

  - 업로드 된 파일의 주소(URL) 를 만들어 주는 역할

  - MEDIA_ROOT 에서 제공되는 미디어 파일을 처리하는 URL
    - 웹 서버 사용자가 사용하는 public URL	
  - 비어 있지 않는 값으로 설정한다면 반드시 slash(/)로 끝나야 함
  - MEDIA_URL 과 STATIC_URL 은 서로 다른 경로를 가져야 한다.

- ##### 필수 !

  - ##### html

    ```django
    <form action="" method="POST" enctype="multipart/form-data">
    ```

  - ##### views.py

    ```python
    form = ArticleForm(request.POST, request.FILES)
    ```

    

### 미디어 파일 제공을 위한 설정 (개발 단계)

- MEDIA_ROOT 경로로 사용자가 업로드 한 미디어 파일을 제공하기 위해 MEDIA_URL 주소 생성

  ```python
  from django.conf import settings
  from django.conf.urls.static import static
  
  urlpatterns = [
  	path('admin/', admin.site.urls),
  	path('articles/', include('articles.urls')),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```



## Thumbnail

- ##### pilkit

  - 이미지를 잘라주는 proccessor 를 pilkit 에서 지원
  - Pillow 를 이용한다.

  ```bash
  pip install pilkit
  pip install django-imagekit
  ```

  - settings.py 의  INTALLED_APPS 에 imagekit 등록

- ##### 원본을 만들지 않고 Thumbnail 만들기

  ##### models.py

  ```python
  from imagekit.models import ProcessedImageField
  from imagekit.processors import Thumbnail
  
  image = ProcessedImageField( # 원본을 사용하지 않을 때 사용
          blank=True,
          processors=[Thumbnail(100, 100)], # 썸네일 크기
          format='JPEG', # jpeg 로 처리
          options={
              'quality': 80, # 기존 이미지를 80% 압축
          }
      )
  ```

  

