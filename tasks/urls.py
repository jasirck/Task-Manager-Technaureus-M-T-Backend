from django.urls import path
from tasks import views
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('tasks/', views.TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', views.TaskUpdateView.as_view(), name='task-update'),#Updations
]
