from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),  # Home page
    path('add/', views.add_task, name='add'),  # Page to add tasks
    path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout page
    path('register/', views.register_view, name='register'),  # Register page
]
