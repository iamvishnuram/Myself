from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('subscribe/', views.Subscribe, name='subscribe'),
    path('success/', views.Successview, name='success'),
    path('profile/', views.Profile, name='profile'),
    path('login/', views.Login, name='login'),
    path('join/', views.Join, name='join'),
    path('logout/', views.logout, name='logout'),
    path('works/', views.Workview, name='work')
]
