from django.urls import path
from . import views

app_name='examples'
urlpatterns = [
    path('dtl_practice/', views.dtl_practice, name='dtl'),
    path('index/', views.index, name='index'),
    path('hello/<name>/', views.hello, name='hello'),
]
