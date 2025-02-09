from django.urls import path
from . import views

urlpatterns = [
    path('show_task/',views.show_task),
    
]
