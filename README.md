1. Django 프로젝트 세팅

가상환경 구축하는 방법 (with Poetry)
Poetry는 Python 패키지 관리 도구로, 의존성 관리와 패키지 배포를 간편하게 처리할 수 있습니다.
가상환경 구축을 위한 기본 명령어:
poetry init          # 새로운 Poetry 프로젝트 초기화
poetry install       # 의존성 설치
poetry shell         # 가상환경 활성화
Poetry는 pyproject.toml을 사용하여 의존성 관리 및 프로젝트 설정을 진행합니다.
2 Django 설치 및 프로젝트 구성, 앱 세팅하는 방법
Django 설치:
poetry add django
Django 프로젝트 생성:
django-admin startproject project_name
cd project_name
3 앱 생성:
python manage.py startapp app_name
4 templates 경로 지정하기
기본적으로 templates 디렉토리는 프로젝트 또는 앱의 디렉토리에 생성됩니다. 이를 settings.py에서 TEMPLATES 설정으로 지정합니다.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 프로젝트의 templates 폴더 경로 지정
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
static 경로 지정하기
static 파일들은 CSS, JS, 이미지 등의 파일을 의미합니다.
settings.py에서 STATIC_URL과 STATICFILES_DIRS를 지정합니다:
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # 프로젝트의 static 폴더 경로 지정

media 경로 지정하기
Media는 파일 업로드와 관련된 파일들을 저장하는 디렉토리입니다.
settings.py에서 MEDIA_URL과 MEDIA_ROOT를 설정합니다:
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # 업로드된 파일들이 저장될 폴더 경로
2. Database Model

데이터베이스 모델 정의하기
Django 모델은 데이터베이스의 테이블을 나타냅니다. 모델 클래스는 django.db.models.Model을 상속하여 정의합니다.
예시:
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
각 필드별 특징 정리하기
CharField: 짧은 문자열을 저장하는 필드, max_length 필요.
TextField: 긴 텍스트를 저장하는 필드.
IntegerField: 정수값을 저장하는 필드.
DateField: 날짜를 저장하는 필드.
BooleanField: True/False 값을 저장하는 필드.
Migration에 대해서 정리하기
Migration은 모델 변경을 데이터베이스에 반영하는 과정입니다.
마이그레이션 만들기:
python manage.py makemigrations
마이그레이션 적용하기:
python manage.py migrate
3. Jinja

Jinja 문법 정리하기
Jinja는 Django 템플릿 엔진에서 사용되는 템플릿 문법입니다.
변수 출력: {{ variable }}
조건문: {% if condition %}...{% endif %}
반복문: {% for item in list %}...{% endfor %}
block 사용법
{% block content %}{% endblock %}: 템플릿에서 다른 템플릿으로부터 내용을 삽입할 수 있게 해주는 구문입니다.
예시:
{% block content %}
<h1>Welcome to the page</h1>
{% endblock %}
extends 사용법
{% extends 'base.html' %}: 부모 템플릿을 확장하여 자식 템플릿에서 내용을 덮어쓰는 방식입니다.
예시:
{% extends 'base.html' %}

{% block content %}
  <p>This is a child template content</p>
{% endblock %}
4. FBV(Function Based View)

FBV란?
FBV는 함수 기반 뷰로, HTTP 요청을 처리하는 함수입니다. Django에서 기본적으로 사용하는 뷰 방식입니다.
간단한 View 메소드 작성법
render: 템플릿을 렌더링하는 함수.
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
redirect: 다른 URL로 리다이렉트하는 함수.
from django.shortcuts import redirect

def redirect_to_home(request):
    return redirect('home')
5. Urls

URL 엔드포인트란?
URL 엔드포인트는 요청된 URL에 따라 실행되는 기능이나 페이지를 정의하는 경로입니다.
urlspatterns
urlpatterns는 URL과 그에 대응하는 뷰 함수를 연결하는 리스트입니다.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
URL Include 개념 및 방법
include()는 다른 urls.py 파일을 포함시키는 방법입니다.
from django.urls import include, path

urlpatterns = [
    path('users/', include('users.urls')),
]
path
path()는 URL 경로를 정의하는 함수입니다. 첫 번째 인자는 URL, 두 번째 인자는 해당 URL에서 실행할 뷰 함수입니다.
path('home/', views.home, name='home')
include
include()는 다른 urls.py를 포함시키는 함수입니다. 프로젝트가 커질수록 앱별로 urls.py 파일을 만들고 이를 include합니다.
urlpatterns = [
    path('blog/', include('blog.urls')),
]
