from django.contrib import admin
from django.urls import path
from vaccine.views import *
from vaccine import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
]
