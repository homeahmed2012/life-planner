from django.urls import path
from day_app import views


urlpatterns = [
    # path('', views.index),
    path('all_days/', views.all_days, name='all_days'),
    # path('delete/<int:goal_id>/', views.delete, name='delete'),
    # path('update/<int:goal_id>/', views.update, name='update'),
    path('day/<int:day_id>/', views.read_day, name='read_day'),
    path('create_report/<int:day_id>', views.create_report, name='create_report'),
    path('update_report/<int:day_id>', views.update_report, name='update_report')
    # path('add/', views.add, name='add_goal')
]
