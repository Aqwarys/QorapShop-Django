from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
]
