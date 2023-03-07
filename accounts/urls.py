from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.prof, name='profile'),
    path('login/', views.Login, name='login'),
]
