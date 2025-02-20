
from django.contrib import admin
from django.urls import path

from quickapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('About/', views.About,name='About'),
    path('gallery/', views.gallery,name='gallery'),
    path('form/', views.form,name='form'),
    path('product/', views.product,name='product'),
]
