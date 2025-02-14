from django.urls import path
from . import views


urlpatterns = [
    path('manager-dashboard/', views.manager_dashboard),
    path('user-dashboard/', views.user_dashboard),
    path('test/', views.test),
    path('create-task/',views.create_task),
    path('view_task/', views.view_task),
    
    
]
