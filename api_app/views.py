from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, authentication_classes

from . import serializers, permissions
from goal_app.models import Goal, Task, Comment
from day_app.models import Day, Report
from django.contrib.auth.models import User
# Create your views here.


class UserProfile(viewsets.ModelViewSet):
    """Create and update users"""
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


class LoginView(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        response = ObtainAuthToken().post(request)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})


class GoalViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GoalSerializer
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        if self.request.query_params.get('main'):
            return Goal.objects.filter(user=self.request.user, parent__isnull=True).order_by('-created_at')

        return Goal.objects.filter(user=self.request.user).order_by('-created_at')


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskSerializer
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        filters = {}
        if self.request.query_params.get('goal'):
            goal = Goal.objects.get(id=self.request.query_params['goal'])
            filters['goal'] = goal

        if self.request.query_params.get('day'):
            day = Day.objects.get(id=self.request.query_params['day'])
            filters['day'] = day

        return Task.objects.filter(user=self.request.user,
                                   **filters).order_by('created_at')


# get all comments for a specific gaol
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    authentication_classes = (TokenAuthentication, )

    def get_queryset(self):
        goal = Goal.objects.get(id=self.request.query_params['goal_id'])
        return Comment.objects.filter(goal=goal)


class DayApi(ListAPIView):
    serializer_class = serializers.DaySerializer
    authentication_classes = (TokenAuthentication, )


    def get_queryset(self):
        return Day.objects.filter(user=self.request.user)


# get and add day report if exist for a specific day
class ReportView(APIView):
    authentication_classes = (TokenAuthentication, )

    def get(self, request, day_id):
        day = Day.objects.get(id=day_id)
        try:
            report = day.report
        except ObjectDoesNotExist:
            return Response({'day': serializers.DaySerializer(day).data})
        
        return Response({'report': serializers.ReportSerializer(report).data, 
                        'day': serializers.DaySerializer(day).data})


    def post(self, request, day_id):
        day = Day.objects.get(id=day_id)
        try:
            report = day.report
            report.content = request.data['content']
        except ObjectDoesNotExist:
            report = Report(content=request.data['content'], day=day)
        report.save()
        return Response(serializers.ReportSerializer(report).data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def get_day_id(request):
    date = request.query_params.get('date')
    print(date)
    day = Day.objects.filter(user=request.user, date=date).first()
    return Response({'id': day.id})


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def get_subgoals(request, id):
    parent = Goal.objects.get(id=id)
    goals = Goal.objects.filter(
        user=request.user,
        parent=parent
        ).order_by('-created_at')
    serializer = serializers.GoalSerializer(goals, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def goal_detail(request, id):
    goal = Goal.objects.get(id=id)
    serializer = serializers.GoalSerializer(goal)
    return Response(serializer.data)

# class ReportViewSet(viewsets.ModelViewSet):
#     serializer_class = serializers.ReportSerializer
#     authentication_classes = (TokenAuthentication, )
#     queryset = Report.objects.all()
        

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def get_user_goals(request):
    user = request.user
    goals = Goal.objects.filter(user=user)

    serializer = serializers.ParentSerializer(goals, many=True)

    return Response(serializer.data)











class TestApis(APIView):
    def get(self, request):
        return Response({'message': 'hello api'})

    def post(self, request):
        return Response({'message': 'hello api'})

