from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.UsersListAPIView.as_view(), name='users-list'),
    path('me/', views.UserUpdateAPIView.as_view(), name='user-details'),
]
