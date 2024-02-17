from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='contactus'),
    path('register/', views.user_reg, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('changepass/', views.change_password, name='change_pass')
]