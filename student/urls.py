from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('stats/', views.stats, name='stats'),
    path('schedule/', views.schedule, name='schedule'),
    path('payment/', views.payment, name='payment'),
]