from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', views.UserProfile)
router.register('login', views.LoginView, base_name='login')
router.register('goal', views.GoalViewSet, base_name='goal')
router.register('task', views.TaskViewSet, base_name='task')
router.register('comment', views.CommentViewSet, base_name='comment')

urlpatterns = [
    path('test/', views.TestApis.as_view(), name='test_api'),
    path('days/', views.DayApi.as_view(), name='day_api'),
    path('report/<int:day_id>/', views.ReportView.as_view(), name='report_api'),
    path('get-day-id/', views.get_day_id, name='get-day-id'),
    path('goal/<int:id>/subgoals/', views.get_subgoals, name='get-subgoals'),
    path('goal-detail/<int:id>/', views.goal_detail, name='get-detail'),
    path('get-user-goals/', views.get_user_goals, name='get-user-goals'),
    # path('report/', views.ReportView.as_view(), name='report_create'),
    path('', include(router.urls))
]