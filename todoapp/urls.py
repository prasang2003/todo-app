from django.urls import path
from .views import home, delete_task, complete_task  
urlpatterns = [
    path('', home, name="home"),  
    path('delete/<int:task_id>/', delete_task, name="delete_task"),
    path('complete/<int:task_id>/', complete_task, name="complete_task"),
]
