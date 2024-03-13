from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_url', views.url_get, name='get_url'),
    path('<str:pk>', views.go, name='go'),
]