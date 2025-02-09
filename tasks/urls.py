from django.urls import path
from . import views

urlpatterns = [
    path('show_task/',views.show_task),
    path('show_task/<int:id>', views.show_specific_task),
    
]
