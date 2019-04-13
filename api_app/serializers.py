from rest_framework import serializers
from django.contrib.auth.models import User
from goal_app.models import Goal, Task, Comment
from day_app.models import Day, Report


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(username=validated_data['username'],
                    email=validated_data['email'])
        user.set_password(validated_data['password'])

        user.save()

        return user


class GoalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goal
        fields = ('id', 'title', 'description', 'total_time', 'total_spend', 'finished_at', 'goal_type')

    def create(self, validated_data):
        """Creates a new goal using a post request."""
        total_time = int(validated_data['total_time']) 
        total_spend = int(validated_data['total_spend']) 
        finished_at = self.context['request'].data['date'] + ' ' + self.context['request'].data['time']
        user = self.context['request'].user
        parent_id = self.context['request'].data.get('parent')
        if parent_id:
            parent = Goal.objects.get(id=parent_id)
            go = Goal.objects.get_or_create(title=validated_data['title'],
                                            description=validated_data['description'],
                                            total_time=total_time,
                                            total_spend=total_spend,
                                            finished_at=finished_at,
                                            user=user,
                                            parent=parent)[0]
        else:
            go = Goal.objects.get_or_create(title=validated_data['title'],
                                            description=validated_data['description'],
                                            total_time=total_time,
                                            total_spend=total_spend,
                                            finished_at=finished_at,
                                            user=user)[0]
        go.save()
        return go

    def update(self, goal, validated_data):

        goal.title = validated_data.get('title', goal.title)
        goal.description = validated_data.get('description', goal.description)
        goal.total_time = validated_data.get('total_time', goal.total_time)
        goal.total_spend = validated_data.get('total_spend', goal.total_spend) 
        finished_at = self.context['request'].data['date'] + ' ' + self.context['request'].data['time']
        goal.finished_at = finished_at
        goal.save()
        return goal



class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'duration', 'task_type', 'time', 'goal')

    def create(self, validated_data):
        user = self.context['request'].user
        day = Day.objects.get_or_create(date=self.context['request'].data['date'],
                                        user=user)[0]
        day.save()
        time = self.context['request'].data['date'] + ' ' + self.context['request'].data['stime']
        task = Task(title=validated_data['title'],
                    description=validated_data['description'],
                    time=time,
                    duration=int(validated_data['duration']),
                    user=user,
                    day=day,
                    task_type=validated_data['task_type'])

        if 'goal' in validated_data:
            task.goal = validated_data['goal']
        # if task.task_type == 'b' and task.goal:
        #     add_time_to_parents(task.goal, task.duration)
        task.save()
        return task


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at')

    def create(self, validated_data):
        goal = Goal.objects.get(id=self.context['request'].data['goal_id'])
        comment = Comment.objects.get_or_create(content=validated_data['content'],
                                                goal=goal)[0]

        comment.save()
        return comment


class DaySerializer(serializers.ModelSerializer):


    class Meta:
        model = Day
        fields = ('id', 'date')


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = ('id', 'content')

#     def create(self, validated_data):
#         report = Report.objects.create()

#     def retrieve(self):
#         return None


class ParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goal
        fields = ('id', 'title')