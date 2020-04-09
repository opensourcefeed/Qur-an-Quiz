from api.models import User, Question, Category, Level, Option
from api.models import Score
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'id', 'password']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'enabled']

class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields = ['name', 'enabled', 'id', 'seq']

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['option', 'is_correct']

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = ['question', 'options']

class ScoreSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()
    level = LevelSerializer()
    class Meta:
        model = Score
        fields = ['score', 'user', 'category', 'level']


