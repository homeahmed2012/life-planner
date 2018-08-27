from django.urls import path
from goal_app import views


urlpatterns = [
    path('all_goals/', views.all_goals, name='all_goals'),
    path('create_goal/', views.create_goal, name='create_goal'),
    path('goal/<int:goal_id>/', views.read_goal, name='read_goal'),
    path('update_goal/<int:goal_id>/', views.update_goal, name='update_goal'),
    path('delete_goal/<int:goal_id>/', views.delete_goal, name='delete_goal'),


    path('all_tasks/', views.all_tasks, name="all_tasks"),
    path('create_task/', views.create_task, name='create_task'),
    path('task/<int:task_id>', views.read_task, name='read_task'),
    path('update_task/<int:task_id>/', views.update_task, name='update_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),


    path('create_comment/<int:goal_id>/', views.create_comment, name='create_comment'),
    path('update_comment/<int:comment_id>/', views.update_comment, name='update_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
