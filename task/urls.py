from django.urls import path

from .views import *


urlpatterns = [
    path('', tasks, name='tasks'),
    path('add/', addtask, name='addtask'),
    path('mark_as_done/<int:pk>', mark_as_done, name='mark_as_done'),
    path('delete_task/<int:pk>', delete_task, name='delete_task')
]