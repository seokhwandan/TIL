from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('fake_google/', views.fake_google, name='google'),
    path('calc/<int:n1>/<int:n2>/', views.calc, name='calc'),
    path('lotto/', views.lotto, name='lotto'),
]
