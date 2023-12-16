from django.urls import path
from rest_framework import routerDefault
from .views import TodoList, TodoDetail

router = routerDefault()
router.urls


urlpatterns = [
    path('todos/', TodoList.as_view(), name='todo_list'),
    #  path('', viewsets.TodoViewSet(), base_name='todo'),
    path('todos/<int:pk>/', TodoDetail.as_view(), name='todo_detail'),
]
