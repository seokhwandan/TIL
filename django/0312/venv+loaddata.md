python -m venv venv ( 가상환경 설정 )

source venv/Scripts/activate ( 활성화 )

deactivate ( 비활성화 )

pip install django ( 가상환경에 django 따로 설치 )

.gitignore ( vscode python django )

django-admin startproject crud .



pip freeze ( 사용하고 있는 라이브러리의 버전과 이름을 확인할 수 있다 )

pip freeze > requirements.txt ( requirements.txt 에 저장 )

pip install -r requirements.txt ( requirements,txt 에 저장되어 있는 라이브러리를 설치 )



README.md 에는 python 버전을 적는다



python manage.py dumpdata --indent 4  movies.movie > movies.json ( 더미데이터 생성 )

fixtures 폴더 생성 < movies.json 넣기

python manage.py makemigrations

python manage.py migrate

python manage.py loaddata movies/movies.json ( movies.json 의 내용을 db에 저장 )

