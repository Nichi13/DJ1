from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.testPageView, name='zero'),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('', views.BasePageView.as_view(), name='base')
]