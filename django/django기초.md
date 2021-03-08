### django 사용 시 필요한 기본적인 명령어

1. `django-admin startproject 프로젝트이름`
   - 프로젝트 생성

2. `python manage.py runserver`
   - 서버 실행

3. `python manage.py startapp articles`
   - app 생성



### 템플릿 확장 하는 방법

1. 확장하는 템플릿이 위치할 폴더를 생성한다. (택 1)
   1. 설정 폴더
   2. 프로젝트 폴더
      - DIRS의 경로를 잘 설정해 줘야 한다. (settings.py)
2. 공통적으로 사용되는 템플릿을 정의한다. (base.html)
   - `block` 을 설정하여 상이한 내용이 오는 공간을 확보한다.



3. 사용한다.
   - 템플릿 상단에 `{% extends 'base.html' %}` 을 추가한다.
     - 반드시 최상단에 위치해야 한다.
   - `block` 사이에 내용을 채워 넣는다.



### URL 분리

1. 설정 폴더의 `urls.py` 에서 분리 준비를 한다.

   - 상단 주석을 참고 !

   ```python
   Including another URLconf
       1. Import the include() function: from django.urls import include, path
       2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
   ```



2. application 폴더에 `urls.py` 파일을 생성

   - 기본 구조를 잡아줘야 함.

   - path 함수를 사용하기 위한 import
   - urlpatterns 라는 리스트 필요



3. application 폴더의 `urls.py` 에 경로를 등록해서 사용한다.