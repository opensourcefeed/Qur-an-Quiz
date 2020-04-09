from api.models import User, Score, Question, Level, Category
from rest_framework import viewsets, permissions, status
from api.serializers import UserSerializer, QuestionSerializer, CategorySerializer
from api.serializers import ScoreSerializer
from api.serializers import LevelSerializer
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.db.models import Q, Max
from django.db.models.expressions import RawSQL
from django.core import serializers
import json


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def login(self, request):
        queryset = User.objects.all().filter(
            (
                Q(phone=request.data['userId']) | 
                Q(email=request.data['userId'])
            ) & 
            Q(password=request.data['password'])
        )
        user = get_object_or_404(queryset)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class QuestionViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    @action(detail=False, methods=['get'], url_path='level/(?P<level>[^/.]+)/category/(?P<category>[^/.]+)')
    def questions(self, request, level, category):
        print (level, category)
        queryset = self.filter_queryset(self.get_queryset()).filter(level__id=level).filter(category__id=category)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class LevelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

    @action(detail=False, methods=['get'], url_path='(?P<level>[^/.]+)/categories')
    def categories(self, request, level=None):
        print(level)
        queryset = Category.objects.all().filter(
            questions__level__id=level
        ).filter(enabled=True).distinct()
        serializer = CategorySerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)

class ScoreViewSet(viewsets.ModelViewSet):

    serializer_class = ScoreSerializer
    queryset = Score.objects.all()

    def retrieve(self, request, pk=None):
        try:
            queryset = Score.objects.all().filter(user__id=pk).order_by('-level', '-score').first()
            serializer = ScoreSerializer(queryset)
            return Response(serializer.data)
        except Exception as e:
            print (e)
            return Response({})

    def create(self, request):
        scoreVal = request.data['score']
        userId = request.data['user_id']
        levelId = request.data['level_id']
        categoryId = request.data['category_id']
        print("{} {} {} {}".format(scoreVal, userId, levelId, categoryId))
        score = None
        try:
            score = Score.objects.get(
                   user__id=userId, 
                   level__id = levelId, 
                   category__id = categoryId
                )
        except Exception as e:
            print("Could not find existing score")

        if not score:
            score = Score()
            score.user_id = userId
            score.level_id = levelId
            score.category_id = categoryId
            score.score = scoreVal
            score.save()
        else:
            if score.score < scoreVal:
                score.score = scoreVal
                score.save()

        serializer = ScoreSerializer(score)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request):
        queryset = self.queryset.raw("""
                                     select id, user_id, level_id, score as score
                                     from (
                                     select 
                                     score.id as id,
                                     user.id as user_id,
                                     level.id as level_id,
                                     level.seq as level,
                                     score.score as score,
                                     row_number() over(partition by user.id order by level.seq desc, score.score desc) rn
                                     from api_score score
                                     join api_level level on level.id = score.level_id
                                     join api_user user on user.id = score.user_id
                                     ) t
                                     where rn = 1
                                     order by level desc, score desc;
                                     """)
        records = []
        rank = 1
        for score in queryset:
            records.append({
                "rank": rank,
                "name": score.user.name,
                "level": score.level.seq,
                "score": score.score
            })
            rank += 1
        return Response(records)


